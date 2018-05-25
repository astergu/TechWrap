#include <vector>
#include "Polygon.h"
using namespace std;


bool isPolygonConvex(const Polygon& polygon) {
    // assume the points are in counter-clockwise order
    vector<Point> points = polygon.points();
    if (points.size() < 3) {
        return false;
    }
    for (int i = 0; i < points.size() - 1; ++i) {

    }
    return true;
}

bool convexAngle(const Point& p1, const Point& p2, const Point& p3) {
    
    double va_y = p1.y() - p2.y();
}

int main() {
    return 0;
}

