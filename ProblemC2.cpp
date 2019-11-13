#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <chrono>
#include <set>

struct Node
{
	int start;
	int end;
	int color;
	int adjacent;

	Node(int start_, int end_, int color_) {
		start = start_;
		end = end_;
		color = color_;
		adjacent = 0;
	}

	void print() {
		std::cout << "Start: " << start << " End: " << end << " Adjacent: " << adjacent << " Color: " << color << std::endl;
	}
};

struct sort_on_end
{
	inline bool operator() (const Node& node1, const Node& node2)
	{
		return (node1.end < node2.end);
	}
};

int findInSet(int number, std::map<int, std::set<int> > bookingsets) {
	for(std::pair<int, std::set<int>> set : bookingsets) {
		if (bookingsets[set.first].find(number) != bookingsets[set.first].end()) {
			return set.first;
		}
	}
	return 0;
}

int main(void) {
	//auto start = std::chrono::high_resolution_clock::now();

	int tot = 0;
	std::string line; std::getline(std::cin, line);
	std::string delimiter = " ";
	int n = std::stoi(line.substr(0, line.find(delimiter)));
	int k = std::stoi(line.substr(line.find(delimiter) + 1, line.size()));

	std::vector<Node> bookings;

	for (std::string line; std::getline(std::cin, line);) {
		int start = std::stoi(line.substr(0, line.find(delimiter)));
		int end = std::stoi(line.substr(line.find(delimiter) + 1, line.size()));
		bookings.push_back(Node(start, end, 0));
	}

	for (int i = 0; i < k + 1; i++) {
		bookings.push_back(Node(-i - 1, -i, k - i));
	}

	std::sort(bookings.begin(), bookings.end(), sort_on_end());

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < bookings.size(); j++) {
			if (bookings[k + i + 1].start >= bookings[bookings.size() - j - 1].end) {
				bookings[k + i + 1].adjacent = bookings.size() - j - 1;
				break;
			}
		}
	}

	std::map<int, std::set<int> > bookingsets;

	for (int i = 0; i < bookings.size(); i++) {
		bookingsets[i] = { i };
	}

	int total = 0;
	for (int i = 0; i < n; i++) {
		int adjacent = bookings[k + 1 + i].adjacent;
		int setIndex = findInSet(adjacent, bookingsets);
		if (setIndex == 0) {
			bookings[k + 1 + i].color = 0;
			bookingsets[findInSet(k + i, bookingsets)].insert(bookingsets[(k + i + 1)].begin(), bookingsets[(k + i + 1)].end());
			bookingsets.erase(k + i + 1);
		}
		else {
			bookings[k + 1 + i].color = bookings[adjacent].color;
			total++;
			bookingsets[findInSet(setIndex - 1, bookingsets)].insert(bookingsets[setIndex].begin(), bookingsets[setIndex].end());
			bookingsets.erase(setIndex);
		}
	}

	std::cout << total << std::endl;

	//auto stop = std::chrono::high_resolution_clock::now();
	//auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
	//std::cout << duration.count() << std::endl;

	return 0;
}