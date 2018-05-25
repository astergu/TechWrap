//
// Created by Peiqin on 22/05/2018.
//

#ifndef TECHWRAP_POINT_H
#define TECHWRAP_POINT_H

class Point {
public:
    Point() {}
    Point(const double x, const double y): _x(x), _y(y) {}
    Point(const Point& point) {
        _x = point.x();
        _y = point.y();
    }

    double x() const { return _x; }
    double y() const { return _y; }
private:
    double _x = 0.0;
    double _y = 0.0;
};

#endif //TECHWRAP_POINT_H
