#include <vector>
#include "Polygon.h"
using namespace std;

bool convexAngle(const Point& p1, const Point& p2, const Point& p3);

bool isPolygonConvex(const Polygon& polygon) {
    // assume the points are in counter-clockwise order
    vector<Point> points = polygon.points();
    if (points.size() < 3) {
        return false;
    }
    for (int i = 1; i < points.size() + 1; ++i) {
        bool sharpAngle = convexAngle(points[i-1], points[i%points.size()], points[(i+1) % points.size()]);
        if (!sharpAngle) {
            return false;
        }
    }
    return true;
}

bool convexAngle(const Point& p1, const Point& p2, const Point& p3) {
    double va_x = p1.x() - p2.x();
    double va_y = p1.y() - p2.y();
    double vb_x = p3.x() - p2.x();
    double vb_y = p3.y() - p2.y();
    return (va_x * vb_y - vb_x * va_y) >= 0;
}

int main() {
    vector<Point> points;

    return 0;
}

