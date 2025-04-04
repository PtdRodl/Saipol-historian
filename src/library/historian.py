import requests
from settings import config

settings = config.settings

def get_historian_token():
    historian_host = settings["historian"]["host"]
    historian_username = settings["historian"]["username"]
    historian_password = settings["historian"]["password"]


    oauth_info = {
    "client_id": "historian_public_rest_api",
    "client_secret": "publicapisecret",
    }

    
    url = f"https://{historian_host}/uaa/oauth/token?grant_type=password&username={historian_username}&password={historian_password}"
    response = requests.post(url, data=oauth_info, verify=False)

    if response.status_code == 200:
        access_token = response.json()["access_token"]
        return access_token
    else:
        raise Exception("Erreur: {} {}".format(response.status_code, response.text))




def get_historian_raw_data(token, start_time, end_time):
    historian_host = settings["historian"]["host"]
    tags_list = settings["tags"]["list"]

    # url = f"https://{historian_host}/historian-rest-api/v1/datapoints/raw/"
    url = f"https://{historian_host}/historian-rest-api/v1/datapoints/interpolated/"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    tags_list_str = ";".join(tags_list)

    params = {
        "tagNames": tags_list_str,
        "start": start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "end": end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        "direction": 0,
        "count": 5,
        "intervalMs": 10000
    }

    response = requests.get(url, headers=headers, params=params, verify=False)

    if response.status_code == 200:
        return response.json()["Data"]
    else:
        raise Exception("Erreur: {} {}".format(response.status_code, response.text))



