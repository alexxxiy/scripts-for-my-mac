#!/usr/local/bin/python3
import argparse
import sqlite3
import requests
import sys
import re
from termcolor import colored
# from langdetect import detect
# from langdetect import detect_langs

import api

# db
from snaql.factory import Snaql
import os

# корень проекта
root_location = os.path.abspath(os.path.dirname(__file__))

# регистрация директории с шаблонами
snaql_factory = Snaql(root_location, 'sql')

# регистрация шаблона с SQL-блоками
queries = snaql_factory.load_queries('queries.sql')


connection = sqlite3.connect(root_location + '/sql/storage.db')
cursor = connection.cursor()

def main(data, source):
	service = getattr(api, source)
	print(service.name)

	table = data['fromLang'] + '_' + data['toLang'] + '_' + source;

	sql = queries.check(table=table, fromText=data['text'])
	cursor.execute(sql)
	cache = cursor.fetchone()

	if cache and not args.force:
		print(cache[0])
	else:
		try:
			result = service.run(data['text'], data['fromLang'], data['toLang'])
			# если результат равен запросу, то скорее всего неверный текст запроса
			if data['text'] == result:
				raise Exception('Что-то пошло не так :(')

			if cache and args.force: sql = queries.update(table=table, fromText=data['text'], toText=result)
			else:                    sql = queries.insert(table=table, fromText=data['text'], toText=result)
			# print(sql)
			cursor.execute(sql)

			print(result)
		except Exception as e:
			print(colored(e, 'red'))

	connection.commit();



# arguments
parser = argparse.ArgumentParser(description='translate text')
parser.add_argument('--force', action='store_true')
parser.add_argument('-y', action='store_true', help='use yandex api')
parser.add_argument('-g', action='store_true', help='use google api')
parser.add_argument('-t', action='store_true', help='use itranslate4 api')
parser.add_argument('-a', action='store_true', help='use all available api')
parser.add_argument('text', type=str, help='text for translate')
args = parser.parse_args()

# print(args)

# text
text = args.text.lower()

# lang detect
ru = re.findall(r'[а-яА-Я]', text)

if len(ru) > 0:
	fromLang = 'ru'
	toLang = 'en'
else:
	fromLang = 'en'
	toLang = 'ru'

# fromLang = detect(text)
# toLang = 'ru'

data = {
	'text': text,
	'fromLang': fromLang,
	'toLang': toLang
}

#default api translator
if not args.y and not args.g and not args.t:
	args.y = True

# api controller
sources = set()
if args.a:
	sources = set(['yandex', 'google', 'itranslate4'])
else:
	if args.y:
		sources.add('yandex')
	if args.g:
		sources.add('google')
	if args.t:
		sources.add('itranslate4')

# call translator()
for source in sources:
	main(data, source)




