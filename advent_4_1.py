import requests

cookie = {'session': '53616c7465645f5f9531a1cfa48d35689f93c460fb25bcd376e0bfaeea195562d7ce6e82497e0972b6fd4e408f5c176f'}

r = requests.get('https://adventofcode.com/2017/day/4/input', cookies = cookie)

count = 0

phrases = r.text.strip().split('\n')
for phrase in phrases:
	phrase_tokens = phrase.split()
	if len(set(phrase_tokens)) == len(phrase_tokens):
		count = count + 1

print count