import sys
import pprint

# For each child find the value of their blood by combining the values
# of the two parents 
# If a parent are royal and we have not yet calculated their blood value
# recursivly traverse upward in the family tree until we can find a value for 
# their blood
def findBloodValue(child, bloodDict):
	# variables for parents and blood values
	blood1 = 0
	blood2 = 0
	parent1 = ""
	parent2 = ""
	# If blood already calculated for the child return it
	if "blood" in bloodDict[child]:
		return bloodDict[child]["blood"]
	# Else check who parents are
	else:
		parent1 = bloodDict[child]["parent1"]
		parent2 = bloodDict[child]["parent2"]
	# If first parent is not royal ignore it
	if parent1 not in bloodDict:
		blood1 = 0
	# Else check or calculate the first parents value by calling the function on parent
	else:
		blood1 = findBloodValue(parent1, bloodDict)

	# If second parent is not royal ignore it
	if parent2 not in bloodDict:
		blood2 = 0
	# Else check or calculate the first parents value by calling the function on parent
	else:
		blood2 = findBloodValue(parent2, bloodDict)

	# Calculate childs bloodvalue by combining the values of the parents
	bloodDict[child]["blood"] = (blood1 + blood2)/2
	return (blood1 + blood2)/2

# Read in the the different variables
input = sys.stdin.readlines()
variables = input[0].split()
n = int(variables[0])
m = int(variables[1])

# Create empty dictionary and add founder
dict = {}
founder = input[1].rstrip()
dict[founder] = {"blood": 1}

# Add the royal children to dictionary
# If these appear as a parent we will need to know their blood value before 
# we can calculate the value of their child
for i in range(n):
	person = input[2 + i].split()
	dict[person[0]] = {"parent1": person[1], "parent2": person[2]}

# For each of the royal children find the blood value by calling the findBloodValue function
for i in range(n):
	person = input[2 + i].split()
	blood = findBloodValue(person[0], dict)


# Check blood values for the people claiming the throne 
# and save the one with highest value
max = 0
heir = ""
for i in range (m):
	person = input[2 + i + n].rstrip()
	if person in dict:
		if dict[person]["blood"] > max:
			max = dict[person]["blood"]
			heir = person

#Print the name of the heir
print(heir)

