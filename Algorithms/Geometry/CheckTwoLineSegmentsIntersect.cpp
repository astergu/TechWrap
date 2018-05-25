/**
 * https://practice.geeksforgeeks.org/problems/check-if-two-line-segments-intersect/0
 *
 * Given the coordinates of the end points of two line segments and you have to check if they intersect or not.
 *
 * Constraints:
 *      1 ≤ T ≤ 300
 *      -1000000 ≤ xi,yi ≤ 1000000    1<=i<= 4
 *
 */

#include <iostream>
using namespace std;

class Point {
public:
    Point(int x, int y):_x(x), _y(y){}
    int x() { return _x; }
    int y() { return _y; }
private:
    int _x;
    int _y;
};

class Vector {
public:
    Vector(Point s, Point e):start(s), end(e) {
       x = e.x() - s.x();
       y = e.y() - s.y();
    }
    Point start;
    Point end;
    int x;
    int y;
};

Vector negative(const Vector& orig) {
    return Vector(orig.end, orig.start);
}

long vector_product(const Vector& a, const Vector& b) {
    return a.x * b.y - b.x * a.y;
}

bool is_intersect(Point a, Point b, Point c, Point d) {
    Vector ac = Vector(a, c);
    Vector ad = Vector(a, d);
    Vector bc = Vector(b, c);
    Vector bd = Vector(b, d);
    Vector ca = negative(ac);
    Vector cb = negative(bc);
    Vector da = negative(ad);
    Vector db = negative(bd);

    return vector_product(ac, ad) * vector_product(bc, bd) <= 0
        && (vector_product(ca, cb) * vector_product(da, db) <= 0);
}

int main() {
    int T = 0;
    cin >> T;
    int x1, y1, x2, y2;
    int x3, y3, x4, y4;
    for (int i = 0; i < T; ++i) {
        cin >> x1 >> y1 >> x2 >> y2;
        cin >> x3 >> y3 >> x4 >> y4;
        cout << is_intersect(Point(x1, y1), Point(x2, y2), Point(x3, y3), Point(x4, y4)) << endl;
    }
    return 0;
}
