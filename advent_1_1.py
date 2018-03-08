import requests

cookies = {"session": "53616c7465645f5f9531a1cfa48d35689f93c460fb25bcd376e0bfaeea195562d7ce6e82497e0972b6fd4e408f5c176f"}
r = requests.get('https://adventofcode.com/2017/day/1/input', cookies = cookies)

sq = list(r.text.strip())

sum = 0

for i in range(len(sq)):
	if i == len(sq) - 1:
		if sq[i] == sq[0]:
			sum = sum + int(sq[i])
	else:
		if sq[i] == sq[i + 1]:
			sum = sum + int(sq[i])
			
print sum
				