import requests
import sys
from src import DSTREAM_API_KEY


def get_dstrem_url():
    try:
        response = requests.get(
            f"https://doodstream.com/api/upload/server?key={DSTREAM_API_KEY}")
        data = response.json()
        if data['msg'] == "Wrong Auth":
            sys.exit("Invalid API key, please check your API key")
        else:
            return data
    except ConnectionError as err:
        sys.exit(f"ERROR : {err}")
