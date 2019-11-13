import sys
import operator
import pprint

contents = sys.stdin.readline()
variables = contents.split()
n = int(variables[0])
k = int(variables[1])
tot = 0


bookings = []

for i in range(n):
	line = sys.stdin.readline()
	tmp = line.split()
	start = (int(tmp[0]))
	end = (int(tmp[1]))
	bookings.append({"start" : start, "end": end, "overlap": [], "color": -1})
	if( i % 1000 == 0):
		print(i)

print("sorting")
bookings.sort(key=operator.itemgetter('end'))
print("done sorting")

for i in range(n):
	colors = []
	for j in range (i):
		if bookings[i]["start"] < bookings[j]["end"] and bookings[i]["end"] > bookings[j]["start"]:
			bookings[i]["overlap"].append(j)
			bookings[j]["overlap"].append(i)
			colors.append(bookings[j]["color"])
	for c in range(k):
		if c not in colors:
			bookings[i]["color"] = c
			tot += 1
			break
	if tot < k:
		bookings[i]["color"] = tot

pprint.pprint(bookings)

print(tot)
