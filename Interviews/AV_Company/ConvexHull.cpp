//
// Created by Peiqin on 21/05/2018.
//

#include "ConvexHull.h"

Polygon ConvexHull::constructPolygon(const std::vector<Point>& points) {
    if (points.size() < 3) {
        return nullptr;
    }
    std::vector<Point> hull_points;
    for (size_t i = 0; i < points.size(); ++i) {
        if (points.at(i))
    }
    return Polygon(hull_points);
}
