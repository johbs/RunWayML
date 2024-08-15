import requests
import time

# Define your API key and endpoint
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://api.runwayml.com/v1'

# Define the endpoints
UPLOAD_ENDPOINT = f'{BASE_URL}/upload'
GENERATE_ENDPOINT = f'{BASE_URL}/generate'
STATUS_ENDPOINT = f'{BASE_URL}/status'
DOWNLOAD_ENDPOINT = f'{BASE_URL}/download'

# Define the file path
FILE_PATH = '~/Documents/step.jpg'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json',
}

def upload_image(file_path):
    files = {'file': open(file_path, 'rb')}
    response = requests.post(UPLOAD_ENDPOINT, headers=headers, files=files)
    return response.json()

def generate_video(upload_id):
    data = {'upload_id': upload_id}
    response = requests.post(GENERATE_ENDPOINT, headers=headers, json=data)
    return response.json()

def check_status(task_id):
    response = requests.get(f'{STATUS_ENDPOINT}/{task_id}', headers=headers)
    return response.json()

def download_video(download_url):
    response = requests.get(download_url, headers=headers, stream=True)
    with open('video.mp4', 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

# Upload the image
upload_response = upload_image(FILE_PATH)
upload_id = upload_response['upload_id']

# Generate the video
generate_response = generate_video(upload_id)
task_id = generate_response['task_id']

# Wait for the video generation to complete
while True:
    status_response = check_status(task_id)
    if status_response['status'] == 'completed':
        download_url = status_response['download_url']
        break
    elif status_response['status'] == 'failed':
        raise Exception('Video generation failed.')
    time.sleep(30)  # Check status every 30 seconds

# Download the video
download_video(download_url)
print('Download completed.')

