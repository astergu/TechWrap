//
// Created by Peiqin on 22/05/2018.
//

#ifndef TECHWRAP_CONVEXHULL_H
#define TECHWRAP_CONVEXHULL_H

#include <vector>
#include "Polygon.h"

class ConvexHull {
    Polygon constructPolygon(const std::vector<Point>& points);
};

#endif //TECHWRAP_CONVEXHULL_H
