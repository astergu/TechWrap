//
// Created by Peiqin on 22/05/2018.
//

#ifndef TECHWRAP_POLYGON_H
#define TECHWRAP_POLYGON_H

#include <vector>
#include "Point.h"

class Polygon {
public:
    Polygon();
    Polygon(const std::vector<Point>& points);
    ~Polygon();
    bool isConvex();
public:
    std::vector<Point> _points;
};

#endif //TECHWRAP_POLYGON_H
