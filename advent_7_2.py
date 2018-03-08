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

def calculate_weight(node):
	weight = int(node.weight)
	for child in node.children:
		weight = weight + calculate_weight(child)
	return weight
	

def validate_weight(node):
	weight = 0
	prev_node = None
	for child in node.children:
		weight_calc = calculate_weight(child)
		if weight == 0:
			weight = weight_calc
		else:
			if weight != weight_calc:
				print 'error at parent node', node, 'prev node', prev_node, 'child', child, 'weight', weight, 'weight_calc', weight_calc
				print 'answer is', int(prev_node.weight) - (weight_calc - weight), 'or', int(child.weight) - (weight_calc - weight)
				print 'answer is', int(prev_node.weight) + (weight_calc - weight), 'or', int(child.weight) + (weight_calc - weight)
				
		prev_node = child
		validate_weight(child)
				
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
validate_weight(root)
		
			