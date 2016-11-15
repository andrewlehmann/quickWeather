import json, requests, sys

if len(sys.argv) < 2:
	print('Usage: weather.py location')
	sys.exit()
location = ' '.join(sys.argv[1:])
