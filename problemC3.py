import sys
import operator
import pprint


def findInSet(number, sets):
	for set in sets:
		if number in sets[set]:
			return set

contents = sys.stdin.readline()
variables = contents.split()
n = int(variables[0])
k = int(variables[1])
tot = 0

bookings = []
bookingsets = {}

for i in range(k+1):
	bookings.append({"start": -i-1, "end": -i, "color": k-i})

for i in range(n):
	line = sys.stdin.readline()
	tmp = line.split()
	start = (int(tmp[0]))
	end = (int(tmp[1]))
	bookings.append({"start" : start, "end": end, "adjacent": 0, "color":0})

for j in range(n):
	for i in range(len(bookings)):
		if bookings[k+1+j]["start"] >= bookings[len(bookings)-i-1]["end"]:
			bookings[k+1+j]["adjacent"] = len(bookings)-i-1
			break

bookings.sort(key=operator.itemgetter('end'))

for i in range(len(bookings)):
	bookingsets[str(i)] = {i}

pprint.pprint(bookings)

tot = 0
for i in range(n):

	adjacent = bookings[k+1+i]["adjacent"]
	setindex = findInSet(adjacent, bookingsets)
	print("adjacent: ", end= " ")
	print(adjacent)
	print("setindex: ", end=" ")
	print(setindex)
	if setindex == '0':
		bookings[k+1+i]["color"] = 0
		bookingsets[findInSet(k+i, bookingsets)] = bookingsets[str(k+i+1)].union(bookingsets[findInSet(k+i, bookingsets)])
		del bookingsets[str(k+i+1)]
	else:
		bookings[k+1+i]["color"] = bookings[adjacent]["color"]
		tot+=1;
		bookingsets[findInSet(int(setindex)-1, bookingsets)] = bookingsets[setindex].union(bookingsets[findInSet(int(setindex)-1, bookingsets)])
		bookingsets.pop(setindex, None)

print(tot)