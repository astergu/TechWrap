#include <iostream>
#include <vector>
#include <cmath>
using namespace std;


struct Point {
    Point(float px, float py): x(px), y(py) {}
    float x;
    float y;

    //bool operator <(const Point& rhs) const {
    //    return x < rhs.x;
    //}
};

// another comparator implementation
bool cmp_x(const Point& p1, const Point& p2) {
    return p1.x < p2.x;
}

bool cmp_y(const Point& p1, const Point& p2) {
    return p1.y < p2.y;
}


float getDistance(const Point& p1, const Point& p2) {
    float dx = p2.x - p1.x;
    float dy = p2.y - p1.y;
    return sqrt(dx * dx + dy * dy);
}

// naive solution
float shortestLineSegment(const vector<Point>& points) {
    /*
     * Time complexity: O(N^2), Space complexity: O(1)
     */
    float minLength = std::numeric_limits<float>::max(); 
    for (int i = 0; i < points.size(); ++i) {
        for (int j = i + 1; j < points.size(); ++j) {
            float segmentLength = getDistance(points[i], points[j]);
            minLength = std::min(segmentLength, minLength);
        }
    }

    return minLength;
}

void printPoints(const vector<Point>& points) {
    for (size_t i = 0; i < points.size(); ++i) {
        cout << "(" << points[i].x << ", " << points[i].y << ")" << endl;
    }
}

float getMin(const vector<Point>& points, int low, int high);

// divide-and-conquer solution
float shortestLineSegmentDC(vector<Point>& points) {
    std::sort(points.begin(), points.end(), cmp_x);
    return getMin(points, 0, points.size() - 1);
}

float getMin(const vector<Point>& points, int low, int high) {
    if (high - low == 1) {
        return getDistance(points[low], points[low + 1]);
    } else if (high - low == 2) {
        float d1 = getDistance(points[low], points[low + 1]); 
        float d2 = getDistance(points[low], points[low + 2]); 
        float d3 = getDistance(points[low + 1], points[low + 2]);
        return std::min(std::min(d1, d2), d3);
    }

    int mid = (low + high) / 2;
    float leftMin = getMin(points, low, mid);
    float rightMin = getMin(points, mid + 1, high);
    float d = std::min(leftMin, rightMin);
    vector<Point> res;
    for (size_t i = low; i <= high; ++i) {
        if (std::fabs(getDistance(points[i], points[mid])) < d) {
            res.push_back(points[i]);
        }
    }
    std::sort(res.begin(), res.end(), cmp_y);

    for (size_t i = 0; i < res.size(); ++i) {
        for (size_t j = i + 1; j < res.size(); ++j) {
            if (res[j].y - res[j].y >= d) {
                break;
            }
            float dp = getDistance(res[i], res[j]);
            if (dp < d) {
                d = dp;
            }
        }
    }
    return d;
}

int main() {
    vector<Point> points;
    points.push_back(Point(1, 2));
    points.push_back(Point(3, 4));
    points.push_back(Point(0, 6));
    points.push_back(Point(2, 5));

    float shortestLength = shortestLineSegmentDC(points);
    cout << "Shortest Line Segment Length: " << shortestLength << endl;
    return 0;
}
