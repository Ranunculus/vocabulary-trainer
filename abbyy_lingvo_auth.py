import requests

auth_url = 'https://developers.lingvolive.com/api/v1.1/authenticate'


def auth_key():
    fh = open("lingvo.api.key")
    return fh.readline().rstrip()


def auth_token():
    headers = {'Authorization': 'Basic ' + auth_key()}
    post = requests.post(auth_url, headers=headers)
    return post.text
