#include <vector>
#include "Polygon.h"
using namespace std;


bool isPolygonClosed(const vector<LineSegment>& segments) {
    if (segments.size() < 3) {
        return false;
    }

    return false;
}


int main() {
    vector<LineSegment> segments;
    segments.push_back(LineSegment(Point(1, 2), Point(3, 4)));
    segments.push_back(LineSegment(Point(1, 5), Point(3, 4)));
    segments.push_back(LineSegment(Point(1, 2), Point(1, 5)));
    return 0;
}
