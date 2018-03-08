import requests

cookie = {'session': '53616c7465645f5f9531a1cfa48d35689f93c460fb25bcd376e0bfaeea195562d7ce6e82497e0972b6fd4e408f5c176f'}

r = requests.get('https://adventofcode.com/2017/day/6/input', cookies = cookie)

banks = map(int, r.text.strip().split())
#banks = [0, 2, 7, 0]
banks_num = len(banks)

print 'banks', banks

history_banks = []

count = 0

history_banks.append(list(banks)) 

try:
	while True:	
		max_num = max(banks)
		max_idx = banks.index(max_num)	
		banks[max_idx] = 0
		max_idx = (max_idx + 1) % banks_num
		while max_num > 0:
			banks[max_idx] = banks[max_idx] + 1
			max_idx = (max_idx + 1) % banks_num	
			max_num = max_num - 1		
			
		count = count + 1							
					
		for history_bank in history_banks:
			if history_bank == banks:
				print 'history already has', banks, 'with count', count
				raise StopIteration
						
		history_banks.append(list(banks)) # to loose reference we need to clone banks with list()
		
		#print 'banks', banks
		
except StopIteration:
	print 'stop'
		
