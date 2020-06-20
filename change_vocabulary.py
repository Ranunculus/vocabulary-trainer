import requests
import json
from abbyy_lingvo_auth import auth_token


def parse_transcription(lingvo_universal_response):
    try:
        return lingvo_universal_response['Body'][0]['Markup'][0]['Text']
    except:
        return lingvo_universal_response['Body'][0]['Items'][0]['Markup'][0]['Markup'][0]['Text']


def parse_translation(response):
    try:
        return response['Body'][1]['Items'][0]['Markup'][1]['Items'][0]['Markup'][0]['Markup'][0]['Text']
    except:
        try:
            return response['Body'][0]['Items'][0]['Markup'][2]['Items'][0]['Markup'][0]['Markup'][0]['Text']
        except:
            return response['Body'][2]['Items'][0]['Markup'][0]['Markup'][0]['Text']


token = auth_token()

words_to_test = ['absolute', 'abstract', 'absurd', 'accessible', 'accident']

for word in words_to_test:
    translate_url = 'https://developers.lingvolive.com/api/v1/Translation?text={0}&srcLang=1033&dstLang=1049&isCaseSensitive=false'.format(
        word)
    headers = {'Authorization': 'Bearer ' + token}
    get_response = requests.get(translate_url, headers=headers).text
    json_response = json.loads(get_response)
    lingvo_universal_response = json_response[0]
    transcription = parse_transcription(lingvo_universal_response)
    print(word)
    print(transcription)
    print(parse_translation(lingvo_universal_response))
