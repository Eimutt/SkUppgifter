#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <chrono>
#include <set>

// Node representing interval
struct Node
{
	int start;
	int end;
	int color;

	Node(int start_, int end_) {
		start = start_;
		end = end_;
		color = -1;
	}
};

// Help method for sorting on nodes on end-time
struct sort_on_end
{
	inline bool operator() (const Node& node1, const Node& node2)
	{
		return (node1.end < node2.end);
	}
};

int main(void) {

	//Read the variables from input
	int tot = 0;
	std::string line; std::getline(std::cin, line);
	std::string delimiter = " ";
	int n = std::stoi(line.substr(0, line.find(delimiter)));
	int k = std::stoi(line.substr(line.find(delimiter)+1, line.size()));

	//Read the intervals and add them to bookings list
	std::vector<Node> bookings;
	for (std::string line; std::getline(std::cin, line);) {
		int start = std::stoi(line.substr(0, line.find(delimiter)));
		int end = std::stoi(line.substr(line.find(delimiter) + 1, line.size()));
		bookings.push_back(Node(start, end));
	}

	// Sort bookinglist on end-time
	std::sort(bookings.begin(), bookings.end(), sort_on_end());

	//For each booking see if any color is available
	//If so add the booking
	int lastc = 0;
	for (int i = 0; i < bookings.size(); i++) {
		std::set<int> colors;
		
		//Check which colors are used by checking overlapping intervals
		for (int j = 0; j < i; j++) {
			if (bookings[i].start < bookings[j].end && bookings[i].end > bookings[j].start) {
				//colors.push_back(bookings[j].color);
				colors.insert(bookings[j].color);
				if (colors.size() > k) {
					break;
				}
			}
		}
		
		//Find next available color by checking which are used
		//Keep track of where we stopped and resume from there in next iteration
		//To get maximum usage out of the colors by varying as much as possible
		//Keep track of how many we add
		bool found = false;
		int startc = lastc;
		for (int c = startc; c < k; c++) {
			//if (std::find(colors.begin(), colors.end(), c) == colors.end()) {
			if (colors.find(c) == colors.end()){
				bookings[i].color = c;
				tot++;
				found = true;
				lastc = c;
				break;
			}
		}
		if (!found) {
			for (int c = 0; c < startc; c++) {
				//if (std::find(colors.begin(), colors.end(), c) == colors.end()) {
				if (colors.find(c) == colors.end()) {
					bookings[i].color = c;
					tot++;
					found = true;
					lastc = c;
					break;
				}
			}
		}
	}

	std::cout << tot << std::endl;

	return 0;
}