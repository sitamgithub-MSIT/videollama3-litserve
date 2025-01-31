import torch
from transformers import AutoModelForCausalLM, AutoProcessor
import litserve as ls


class VideoLLaMA3API(ls.LitAPI):
    """
    VideoLLaMA3API is a subclass of ls.LitAPI that provides an interface to the VideoLLaMA3 model.

    Methods:
        - setup(device): Initializes the model and processor with the specified device.
        - decode_request(request): Convert the request payload to model input.
        - predict(conversation): Uses the model to generate a response for the given input video and question.
        - encode_response(output): Convert the model output to a response payload.
    """

    def setup(self, device):
        """
        Sets up the model and processor for the task.
        """
        model_name = "DAMO-NLP-SG/VideoLLaMA3-2B"
        self.model = AutoModelForCausalLM.from_pretrained(
            model_name,
            trust_remote_code=True,
            device_map={"": device},
            torch_dtype=torch.bfloat16,
            attn_implementation="flash_attention_2",
        )
        self.processor = AutoProcessor.from_pretrained(
            model_name, trust_remote_code=True
        )

    def decode_request(self, request):
        """
        Convert the request payload to conversation template for the model.
        """
        # Extract the video path and question from the request
        video_path = request.get("video_path")
        question = request.get("question")

        # Prepare the conversation template
        return [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": [
                    {
                        "type": "video",
                        "video": {
                            "video_path": video_path,
                            "fps": 1,
                            "max_frames": 128,
                        },
                    },
                    {"type": "text", "text": question},
                ],
            },
        ]

    def predict(self, conversation):
        """
        Run inference and generate response for the given video and question inputs.
        """
        # Run with torch inference mode
        with torch.inference_mode():
            inputs = self.processor(
                conversation=conversation,
                add_system_prompt=True,
                add_generation_prompt=True,
                return_tensors="pt",
            )
            inputs = {
                k: v.to(self.device) if isinstance(v, torch.Tensor) else v
                for k, v in inputs.items()
            }
            if "pixel_values" in inputs:
                inputs["pixel_values"] = inputs["pixel_values"].to(torch.bfloat16)

            # Generate a response from the model
            output_ids = self.model.generate(**inputs, max_new_tokens=128)
            return self.processor.batch_decode(output_ids, skip_special_tokens=True)[0].strip()

    def encode_response(self, output):
        """
        Convert the model output to a response payload.
        """
        return {"response": output}


if __name__ == "__main__":
    # Create an instance of the VideoLLaMA3API and run the LitServer
    api = VideoLLaMA3API()
    server = ls.LitServer(api, track_requests=True)
    server.run(port=8000)
