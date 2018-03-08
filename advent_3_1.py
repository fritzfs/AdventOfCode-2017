from math import sqrt, ceil, floor

MOVE_START = 0
MOVE_UP = 1
MOVE_DOWN = 2
MOVE_LEFT = 3
MOVE_RIGHT = 4

target, number = 361527, 361527

# setup matrix
w = int(ceil(sqrt(number))) # w = h

matrix = [[0 for i in range(w)] for j in range(w)]

x0 = int(round(w/2.0)) - 1
y0 = w/2 + 1 - 1

x = x0
y = y0
matrix[y][x] = 1
move = MOVE_START

for i in range(2, number + 1):	
	if move == MOVE_START:
		move = MOVE_RIGHT
		x = x + 1
	elif move == MOVE_RIGHT:
		if matrix[y-1][x] == 0:
			y = y -1
			move = MOVE_UP
		else:
			x = x + 1
	elif move == MOVE_UP:
		if matrix[y][x-1] == 0:
			x = x -1
			move = MOVE_LEFT
		else:
			y = y - 1
	elif move == MOVE_LEFT:
		if matrix[y+1][x] == 0:
			y = y + 1
			move = MOVE_DOWN
		else:
			x = x - 1
	elif move == MOVE_DOWN:
		if matrix[y][x+1] == 0:
			x = x + 1
			move = MOVE_RIGHT
		else:
			y = y + 1
			
	matrix[y][x] = i

# print matrix
for i in range(w):
	pass
	# print matrix[i]

# find target coordinates	
for i in range(w):
	for j in range(w):
		if matrix[i][j] == target:
			y1 = i
			x1 = j
			break

steps = 0
if x0 < x1:
	steps = x1 - x0
elif x1 < x0:
	steps = x0 - x1
if y0 < y1:
	steps = steps + y1 - y0
elif y1 < y0:
	steps = steps + y0 - y1

print steps
	




