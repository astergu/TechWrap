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

    const double x() const { return _x; }
    const double y() const { return _y; }
private:
    double _x;
    double _y;
};

#endif //TECHWRAP_POINT_H
