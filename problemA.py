import sys



# Update the board state by iterating over the commands
# And check validity at each step
def solve(a):
	direction = 0
	pos = [7, 0]
	a[7][0] = '.'
	for i in contents[8]:
		# If F move in the current direction
		if 'F' in i:
			if direction == 0:
				pos[1] += 1
			elif direction == 1:
				pos[0] -= 1
			elif direction == 2:
				pos[1] -= 1
			elif direction == 3:
				pos[0] += 1
			# Check if new position is out of bounds
			if pos[0] > 7 or pos[0] < 0 or pos[1] < 0 or pos[1] > 7:
				print("Bug!")
				return
			# Check if new position not a valid location
			if '.' not in a[pos[0]][pos[1]] and 'D' not in a[pos[0]][pos[1]]:
				print("Bug!")
				return
		# If L turn left
		elif 'L' in i:
			direction = (direction + 1) % 4
		# If R turn left
		elif 'R' in i:
			direction = (direction - 1) % 4
		# If X attept to destroy ice castle in forward direction
		elif 'X' in i:
			#print("shoot")
			target = pos.copy()
			if direction == 0:
				target[1] += 1
			elif direction == 1:
				target[0] -= 1
			elif direction == 2:
				target[1] -= 1
			elif direction == 3:
				target[0] += 1
			# Check if target is ice castle
			if 'I' not in a[target[0]][target[1]]:
				print("Bug!")
				return
			else:
				a[target[0]][target[1]] = '.'


	# Check if turtle ends on the diamond
	if 'D' in a[pos[0]][pos[1]]:
		print("Diamond!")
	else:
		print("Bug!")


#Read in the boardstate and store in matrix
contents = sys.stdin.readlines()
a = [[0] * 8 for i in range(8)]
for i in range(8):
	for j in range(8):
		a[i][j] = contents[i][j]

solve(a)