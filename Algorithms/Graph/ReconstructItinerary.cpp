/**
 * Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.

Example 1:

    Input: tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:

    Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
    Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
 *
 */

#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <string>
//#include <multiset>
using namespace std;

class Solution {
public:
    void visit(string src, map<string, multiset<string> >& targets, vector<string>& route) {
        while (targets[src].size()) {
            string next = *targets[src].begin();
            targets[src].erase(targets[src].begin());
            visit(next, targets, route);
        }
        route.push_back(src);
    }


    vector<string> findItinerary(vector<pair<string, string> > tickets) {
        map<string, multiset<string> > targets;
        vector<string> route;

        for (auto ticket : tickets) {
            targets[ticket.first].insert(ticket.second);
        }
        visit("JFK", targets, route);
        return vector<string>(route.rbegin(), route.rend());;
    }
};


int main() {
    vector<pair<string, string> > tickets;
    tickets.push_back(std::make_pair("JFK","SFO"));
    tickets.push_back(std::make_pair("ATL","SFO"));
    tickets.push_back(std::make_pair("JFK","ATL"));
    tickets.push_back(std::make_pair("SFO","ATL"));
    tickets.push_back(std::make_pair("ATL","JFK"));
    //tickets.push_back(std::make_pair("JFK", "KUL"));
    //tickets.push_back(std::make_pair("JFK", "NRT"));
    //tickets.push_back(std::make_pair("NRT", "JFK"));

    Solution s;
    vector<string> ret = s.findItinerary(tickets);
    for (int i = 0; i < ret.size(); i++) {
        cout << ret[i] << endl;
    }

    return 0;
}
