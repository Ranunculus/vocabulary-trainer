import requests


def auth_key():
    with open("lingvo.api.key") as fh:
        return fh.readline().rstrip()


def auth_token():
    auth_url = 'https://developers.lingvolive.com/api/v1.1/authenticate'
    headers = {'Authorization': 'Basic ' + auth_key()}
    post = requests.post(auth_url, headers=headers)
    return post.text
