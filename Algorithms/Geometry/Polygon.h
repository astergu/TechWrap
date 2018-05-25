#ifndef TECHWRAP_POLYGON_H
#define TECHWRAP_POLYGON_H

#include <vector>
#include "Point.h"

class LineSegment {
public:
    LineSegment(const Point& pstart, const Point& pend) : start(pstart), end(pend) {} 

public:
    Point start;
    Point end;
};

class Polygon {
public:
    Polygon();
    Polygon(const std::vector<LineSegment>& segments);
    Polygon(const std::vector<Point>& points);
    ~Polygon();
    
    std::vector<Point> points() const {return _points; };
public:
    std::vector<Point> _points;
};

#endif //TECHWRAP_POLYGON_H
