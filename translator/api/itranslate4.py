#!/usr/local/bin/python3
import requests
from termcolor import colored

conf = {
    'url': 'http://itranslate4.eu/api/Translate',
    'key': '48b42c69-6b34-4202-a4e5-82222222f6f8'
}

name = colored('\niTranslate4', 'green')

def run(text, fromLang='en', toLang='ru'):
	res = requests.get(conf.get('url') + '?auth=' + conf.get('key') + '&src=' + fromLang + '&trg=' + toLang + '&dat=' + text)
	result = res.json()['dat'][0]['text'][0]
	return result