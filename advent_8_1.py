import requests
import re
import sys

cookie = {'session': '53616c7465645f5f9531a1cfa48d35689f93c460fb25bcd376e0bfaeea195562d7ce6e82497e0972b6fd4e408f5c176f'}

r = requests.get('https://adventofcode.com/2017/day/8/input', cookies = cookie)

lines = r.text.strip().split('\n')

regs = {}

for line in lines:
	reg, op, val, if_reg, if_op, if_val = re.match('(\w+) (\w+) ([-\d]+) if (\w+) ([!<>=]+) ([-\d]+)', line).groups()
	val = int(val)
	if_val = int(if_val)
	if regs.has_key(if_reg) == False:
		regs[if_reg] = 0
	if_reg_val = regs[if_reg] 
	if_result = None
	if if_op == '>':
		if_result = if_reg_val > if_val
	elif if_op == '<':
		if_result = if_reg_val < if_val
	elif if_op == '>=':
		if_result = if_reg_val >= if_val
	elif if_op == '<=':
		if_result = if_reg_val <= if_val	
	elif if_op == '==':
		if_result = if_reg_val == if_val		
	elif if_op == '!=':
		if_result = if_reg_val != if_val				
	else:
		print 'unknown if_op', if_op, 'on line', line
		sys.exit(1)
	if if_result:		
		if regs.has_key(reg) == False:
			regs[reg] = 0
		if op == 'inc':
			regs[reg] = regs[reg] + val
		elif op == 'dec':
			regs[reg] = regs[reg] - val
		else:
			print 'unknown op', op, 'on line', line
			sys.exit(1)

max_reg = regs.items()[0][0]
max_val = regs.items()[0][1]

for k, v in regs.items():
	if v > max_val:
		max_reg = k
		max_val = v
		
print 'max value', max_val, 'in', max_reg