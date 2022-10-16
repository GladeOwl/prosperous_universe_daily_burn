import json
import os
import requests
from dotenv import load_dotenv


def write_to_file(data: dict):
    pass


def get_authtoken():
    url: str = "https://rest.fnar.net/auth/login"
    data: dict = {
        "UserName": os.environ.get("USER"),
        "Password": os.environ.get("PASS"),
    }
    response: dict = requests.post(url=url, json=data).json()
    write_to_file(response)
    return response["AuthToken"]
