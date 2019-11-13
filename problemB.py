import sys
import pprint

input = sys.stdin.readlines()

va = input[0].split()
n = int(va[0])
m = int(va[1])

dict = {}
king = input[1].rstrip()
dict[king] = {"gen": 1, "blood": 1}

for i in range(n):
	line = input[2 + i].split()
	gen = 0
	if line[1] in dict:
		gen = dict[line[1]]["gen"] + 1
	if line[2] in dict:
		if (dict[line[2]]["gen"] + 1) > gen:
			gen = dict[line[2]]["gen"] + 1
	dict[line[0]] = {"parent1": line[1], "parent2": line[2], "gen": gen, "blood" : 0}

for child in (sorted(dict, key = lambda child: dict[child]["gen"])):
	childobj = dict[child]
	if childobj["gen"] > 1:
		blood1 = 0
		blood2 = 0
		if childobj["parent1"] not in dict:
			blood1 = 0
			blood2 = dict[childobj["parent2"]]["blood"]
		elif childobj["parent2"] not in dict:
			blood2 = 0
			blood1 = dict[childobj["parent1"]]["blood"]
		else:
			blood1 = dict[childobj["parent1"]]["blood"]
			blood2 = dict[childobj["parent2"]]["blood"]

		dict[child]["blood"] = (blood1 + blood2)/2



max = 0
hier = ""

for i in range(m):
	line = input[2 + n + i].rstrip()
	if line not in dict:
		continue	
	if dict[line]["blood"] > max:
		hier = line
		max = dict[line]["blood"]

pprint.pprint(dict)
print(hier)
