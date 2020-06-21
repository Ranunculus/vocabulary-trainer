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


def get_word_data(words):
    token = auth_token()
    results = []
    for word in words:
        print("Processing: ", word)
        json_response = None
        result = dict()
        try:
            translate_url = 'https://developers.lingvolive.com/api/v1/Translation?text={0}&srcLang=1033&dstLang=1049&isCaseSensitive=false'.format(word)
            headers = {'Authorization': 'Bearer ' + token}
            get_response = requests.get(translate_url, headers=headers).text
            json_response = json.loads(get_response)
            if json_response == 'Incoming request rate exceeded for 50000 chars per day pricing tier':
                print('Exceeded daily limit')
                break
            lingvo_universal_response = json_response[0]
            result["word"] = word
            result["transcription"] = parse_transcription(lingvo_universal_response)
            result["translation"] = parse_translation(lingvo_universal_response)
            results.append(result)
        except Exception as ex:
            print(ex)
            print("can't parse", json_response)
    return results
