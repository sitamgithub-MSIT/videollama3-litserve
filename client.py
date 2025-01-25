import requests

url = "http://localhost:8000/predict"

# Example video path and question
video_path = "videos/bear.mp4"
question = "What is unusual in the video?"

# Prepare the request payload
payload = {
    "video_path": video_path,
    "question": question,
}

# Send the request to the server
response = requests.post(url, json=payload)

# Print the JSON response
print(response.json())
