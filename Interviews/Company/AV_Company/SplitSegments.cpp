#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

namespace map {

struct Point {
    Point(float px, float py) : x(px), y(py) {}
    float x, y;
};

typedef vector<Point> PointVector;

float calculateDistance(const Point& v1, const Point& v2) {
    float dx = v2.x - v1.x;
    float dy = v2.y - v1.y;
    return sqrt(dx * dx + dy * dy);
}

void displayDistance(const PointVector& pv, float* ds) {
    for (size_t i = 0; i < pv.size() - 1; ++i) {
        *ds += calculateDistance(pv[i], pv[i + 1]);
    }
    cout << "total distance: " << *ds << endl;
}

Point findMiddlePoint(const Point& start, const Point& end, const float offset) {
    float len = calculateDistance(start, end);
    float ratio = offset / len;
    float rx = start.x + (end.x - start.x) * ratio;
    float ry = start.y + (end.y - start.y) * ratio;
    return Point(rx, ry);
}

void splitSegments(const PointVector& pv, vector<PointVector>& segments) {
    vector<int> accuDist(pv.size());
    accuDist[0] = 0.0;
    for (size_t i = 1; i < pv.size(); ++i) {
        accuDist[i] = calculateDistance(pv[i - 1], pv[i]) + accuDist[i - 1];
    }
    // accu: [0, 1, 2, 3]
    float halfLength = accuDist[accuDist.size() - 1] / 2; // half = 1.5
    int low = 0;
    int high = accuDist.size() - 1;
    int mid = (low + high) / 2;
    while (low < high) {
        if (accuDist[mid] == halfLength) {
            break;
        } else if (accuDist[mid] > halfLength) {
            high = mid - 1;
        } else {
            low = mid;
        }
    }
    float offset = halfLength - accuDist[mid];
    vector<PointVector>::iterator it = segments.begin();
    if (offset < 1e-7) { // split point right at the end of one segment
        PointVector v1(pv.begin(), pv.begin() + mid);
        PointVector v2(pv.begin() + mid, pv.end());
        segments.push_back(v1);
        segments.push_back(v2);
    } else { 
        Point midPoint = findMiddlePoint(pv[mid], pv[mid + 1], offset);
        PointVector v1(pv.begin(), pv.begin() + mid);
        v1.push_back(midPoint);
        PointVector v2(pv.begin() + mid + 1, pv.end());
        v2.insert(v2.begin(), midPoint);
        segments.push_back(v1);
        segments.push_back(v2);
    }
}

void splitSegmentsRecursive(const PointVector& pv, vector<PointVector>& segments) {
}

}

int main() {
    map::PointVector pv;
    pv.push_back(map::Point(1, 1));
    pv.push_back(map::Point(1, 2));
    pv.push_back(map::Point(1, 3));
    pv.push_back(map::Point(1, 4));

    float ds = 0.0;
    displayDistance(pv, &ds);

    vector<map::PointVector> segments;
    splitSegments(pv, segments);

    return 0;
}
