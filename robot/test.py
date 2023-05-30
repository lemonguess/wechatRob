import json
import requests
import os


def send_message(media_id):
    headers = {
        "Content-Type": "application/json"
    }
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=7d1e7b25-fa81-4524-bf3a-5b9030bb9068"
    data = {
        "msgtype": "file",
        "file": {
            "media_id": media_id
        }
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    print(response.text)
    print(response)
def get_media_id():
    file_path = "傅情.txt"
    filelength = os.path.getsize(file_path)
    headers = {
        # "Content-Type": "application/json",
        # "Content-Length": str(filelength),
        "Content-Disposition": f'form-data; name="media";filename="{file_path}"; filelength={filelength}',
        "Content-Type": "application/octet-stream"

    }
    f = open(file_path, 'rb')
    url = "https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key=7d1e7b25-fa81-4524-bf3a-5b9030bb9068&type=file"
    files = {"file": f}
    response = requests.post(url,
                             # headers=headers,
                             files=files)
    print(response.text)
    print(response)
    return response.json().get('media_id')
if __name__ == '__main__':
    media_id = get_media_id()
    send_message(media_id)
