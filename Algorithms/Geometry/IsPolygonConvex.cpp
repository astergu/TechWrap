#include <vector>
#include "Polygon.h"
using namespace std;


bool isPolygonConvex(const Polygon& polygon) {
    // assume the points are in counter-clockwise order
    vector<Point> points = polygon.points();
    if (points.size() < 3) {
        return false;
    }
}


