# VideoLLaMA3 LitServe

[![Open In Studio](https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg)](https://lightning.ai/sitammeur/studios/videollama3-litserve)

[VideoLLaMA 3](https://huggingface.co/collections/DAMO-NLP-SG/videollama3-678cdda9281a0e32fe79af15) is a cutting-edge series of multimodal foundation models mastering image and video comprehension. Its advanced architecture enables superior processing and interpretation of visual data in diverse settings. These models tackle complex challenges like integrating text and visuals, analyzing video sequences, and performing high-level reasoning across static and dynamic scenes. This project shows how to create a self-hosted, private API that deploys the VideoLLaMA 3 [multimodal model](https://huggingface.co/DAMO-NLP-SG/VideoLLaMA3-2B) with LitServe, an easy-to-use, flexible serving engine for AI models built on FastAPI.

## Project Structure

The project is structured as follows:

- `server.py`: The file containing the main code for the web server.
- `client.py`: The file containing the code for client-side requests.
- `LICENSE`: The license file for the project.
- `README.md`: The README file that contains information about the project.
- `assets`: The folder containing screenshots for working on the application.
- `videos`: The folder containing videos for working on the application.
- `.gitignore`: The file containing the list of files and directories to be ignored by Git.

## Tech Stack

- Python (for the programming language)
- PyTorch (for the deep learning framework)
- Hugging Face Transformers Library (for the model)
- LitServe (for the serving engine)

## Getting Started

To get started with this project, follow the steps below:

1. Run the server: `python server.py`
2. Upon running the server successfully, you will see uvicorn running on port 8000.
3. Open a new terminal window.
4. Run the client: `python client.py`

Now, you can see the model's output based on the input request. The model will generate answers based on the input video and question.

## Usage

The project can be used to serve the VideoLLaMA 3 model using LitServe. It allows you to input a video and a question and then get the model's answer. It suggests potential uses in video analysis, visual question answering, and more.

## Contributing

Contributions are welcome! If you would like to contribute to this project, please raise an issue to discuss the changes you want to make. Once the changes are approved, you can create a pull request.

## License

This project is licensed under the [Apache-2.0 License](LICENSE).

## Contact

If you have any questions or suggestions about the project, feel free to contact me on my GitHub profile.

Happy coding! 🚀
