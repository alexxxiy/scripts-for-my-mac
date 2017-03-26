#!/usr/local/bin/python3
import requests
from termcolor import colored
import goslate

name = colored('\nGoogle', 'blue')

def run(text, fromLang='en', toLang='ru'):
	gs = goslate.Goslate()
	res = gs.translate(text, toLang)
	return res
