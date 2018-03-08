import requests

cookie = {'session': '53616c7465645f5f9531a1cfa48d35689f93c460fb25bcd376e0bfaeea195562d7ce6e82497e0972b6fd4e408f5c176f'}

r = requests.get('https://adventofcode.com/2017/day/2/input', cookies = cookie)

sum = 0

rows = r.text.strip().split('\n')
for row in rows:
	numbers = row.split('\t')
	numbers_int = map(int, numbers)
	max_num = max(numbers_int)
	min_num = min(numbers_int)
	sum = sum + (max_num - min_num)
	
print sum