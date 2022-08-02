from src import DSTREAM_API_KEY
from src.functions.get_dstream_uri import get_dstrem_url
import requests


def upload_vid(path):
    url = get_dstrem_url()["result"]
    post_data = {"api_key": DSTREAM_API_KEY}
    filename = path.split("/")[-1]
    post_files = {"file": (filename, open(path, "rb"))}
    res = requests.post(url, data=post_data, files=post_files).json()
    return res
