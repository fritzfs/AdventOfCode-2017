import requests
import re

class Node:

	def __init__(self, name, weight):
		self.name = name
		self.weight = weight
		self.children = []		
		
	def __str__(self):
		return '%s (%s)' % (self.name, self.weight)
		
	def print_tree(self, level = 0):		
		print '\t' * level, self
		for child in self.children:
			child.print_tree(level + 1)

def find_node(name, node):
	if name == node.name:
		return node
	else:
		for child in node.children:
			node = find_node(name, child)
			if node:
				return node
			
cookie = {'session': '53616c7465645f5f9531a1cfa48d35689f93c460fb25bcd376e0bfaeea195562d7ce6e82497e0972b6fd4e408f5c176f'}

r = requests.get('https://adventofcode.com/2017/day/7/input', cookies = cookie)

lines = r.text.strip().split('\n')

root = Node('root', 0)

for line in lines:
	name, weight = re.match('(\w+) .(\d+).', line).groups()
	node = Node(name, weight)
	root.children.append(node)

for line in lines:
	name = re.match('(\w+) .(\d+).', line).groups()[0]
	parent = find_node(name, root)
	has_children = '->' in line	
	if has_children:	
		children = line[line.index('-> ') + 2:].split(',')
		for child in children:
			child = child.strip()
			for node in root.children:
				if child == node.name:
					root.children.remove(node)
					parent.children.append(node)

root.print_tree()