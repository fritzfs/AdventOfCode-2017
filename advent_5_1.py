import requests

cookie = {'session': '53616c7465645f5f9531a1cfa48d35689f93c460fb25bcd376e0bfaeea195562d7ce6e82497e0972b6fd4e408f5c176f'}

r = requests.get('https://adventofcode.com/2017/day/5/input', cookies = cookie)

jumps = map(int, r.text.split())

steps = 0

ptr = jumps[0]

while True:		
	val = jumps[ptr]
	jumps[ptr] = jumps[ptr] + 1
	ptr = ptr + val
	steps = steps + 1
	if ptr < 0 or ptr >= len(jumps):
		print 'exit, steps', steps
		break		
	
	
	