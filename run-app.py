#!/usr/local/bin/python3
# usage:
# app <approximate application name>
# example:
# app ggl --> start Google Chrome
#
# if found more then one app its printed without start
# 

import sys
import os
import glob
import re
from termcolor import colored

# pathes where stored *.app
dirs = [
	'/Applications/',
	'/Applications/Utilities/',
	'/Users/alexiy/Applications/'
	]

def clearAppName(appFullName, path):
	res = appFullName.replace(path, '')
	res = res.replace('.app', '')
	return res.lower()

def getPattern(string):
	pattern = '.*'
	for w in string:
		pattern = pattern + w + '.*'

	return pattern

# print(sys.argv[1])
# print(len(sys.argv))

args = sys.argv
length = len(args)

applications = []

for path in dirs:
	a = glob.glob(path + '*.app')
	a = [[clearAppName(app, path), app] for app in a]
	applications.extend(a)

applications.sort(key=lambda app: app[0])

# print(applications)

if(length == 1):
	print('\n'.join([app[0] for app in applications]))
elif(length == 2):
	arg2 = args[1]
	results = []
	for app in applications:
		r = re.findall(getPattern(arg2), app[0])
		if len(r) > 0:
			results.append(app)
	# print(results)
	if len(results) == 0: print('\x1b[31mApps not found\x1b[0m')
	if len(results) == 1:
		print(colored('Starting ' + results[0][0], 'green', attrs=['bold']))
		os.system('open ' + results[0][1].replace(' ', '\ '))
	elif len(results) > 1:
		for app in results:
			printApp = app[0]
			for char in arg2:
				printApp = re.sub(char, colored(char, 'red', attrs=['bold']), printApp, 1)
			print(printApp)




