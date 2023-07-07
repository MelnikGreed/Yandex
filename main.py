import requests
import os.path
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": "/gorod.jpg"}
        headers = {"Authorization": "OAuth " +token}
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        url = data['href']
        with open(file_path, 'rb') as f:
            response = requests.post(url, files={'file': f})
if __name__ == '__main__':
    path_to_file = os.path.abspath('C:\HW\gorod.jpg')
    token = open('token').read()
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
