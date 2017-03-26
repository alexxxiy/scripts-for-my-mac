#!/usr/local/bin/python3
import requests
from termcolor import colored


conf = {
	'url': 'https://translate.yandex.net/api/v1.5/tr.json/translate',
	'key': 'trnsl.1.1.20170305T072548Z.e164dc4e249385e0.2f4e07b4d0f71a9b5670317e06af8e9b1ec4e312'
}

name = colored('\nYandex', 'red')

def run(text, fromLang='en', toLang='ru'):
	response = requests.get(conf.get('url') + '?key=' + conf.get('key') + '&lang=' + toLang + '&text=' + text)
	result = response.json()['text'][0]
	return result
