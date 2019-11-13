import sys
import operator
import pprint

def tryadd(booking, list, k):
	cliqueN = 0;
	for i in range(len(list)):
		if booking["start"] < list[len(list)-i-1]["end"] and booking["end"] > list[len(list)-i-1]["start"]:
			cliqueN += 1
		if cliqueN >= k:
			return
		if booking["start"] > list[len(list)-i-1]["end"]:
			break
	list.append(booking)
	return

contents = sys.stdin.readline()
variables = contents.split()
n = int(variables[0])
k = int(variables[1])
tot = 0

bookings = []
included = []

for i in range(n):
	line = sys.stdin.readline()
	tmp = line.split()
	start = (int(tmp[0]))
	end = (int(tmp[1]))
	bookings.append({"start" : start, "end": end})

bookings.sort(key=operator.itemgetter('end'))

for i in range(n):
	tryadd(bookings[i],included, k)

print(len(included))
