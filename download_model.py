import requests
import os

def download_file_from_google_drive(file_id, destination):
    def get_confirm_token(response):
        for key, value in response.cookies.items():
            if key.startswith('download_warning'):
                return value
        return None

    URL = "https://docs.google.com/uc?export=download"
    session = requests.Session()

    response = session.get(URL, params={'id': file_id}, stream=True)
    token = get_confirm_token(response)

    if token:
        params = {'id': file_id, 'confirm': token}
        response = session.get(URL, params=params, stream=True)

    with open(destination, "wb") as f:
        for chunk in response.iter_content(32768):
            if chunk:
                f.write(chunk)

if __name__ == "__main__":
    file_id = "1sVTPyfr-4HSMK7QlUyR5igMbLvR8tE_A"  # your model.pkl file ID
    destination = "model.pkl"

    # Only download if file doesn't already exist
    if not os.path.exists(destination):
        download_file_from_google_drive(file_id, destination)
    else:
        print("model.pkl already exists. Skipping download.")
