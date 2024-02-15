#include <iostream>
#include <vector>
#include <string>
using namespace std;

struct Point {
    Point(int x, int y, float score) {
        this->x = x;
        this->y = y;
        this->score = score;
        this->distance_sq = x * x + y * y;
    }
    
    bool operator <(const Point& rhs) const {
        return distance_sq < rhs.distance_sq;
    }

    std::string toString() {
        return "(" + to_string(x) + ", " + to_string(y) + ": " + to_string(score) + ")";
    }


    int x;
    int y;
    float score;
    int distance_sq;
};

std::ostream& operator<<(std::ostream &strm, const Point& p) {
    return strm << "(" << p.x << ", " << p.y << ": " << p.score  << ")";
}

void printPointVec(const vector<Point>& points) {
    for (size_t i = 0; i < points.size(); ++i) {
        cout << points[i] << " ";
    }
    cout << endl;
}

void maxScoreCircle(vector<Point>& points, float* radian, float* score) {
    std::sort(points.begin(), points.end());
    //printPointVec(points);
    float accu_score = 0.0; 
    int curr_radian = 0; 
    for (size_t i = 0; i < points.size(); ++i) {
        int distance = points[i].distance_sq;
        if (distance > curr_radian) {
            if (accu_score > 1e-7) {
                *score += accu_score;
                accu_score = 0;
                *radian = curr_radian;
            }
            curr_radian = distance; 
        }
        accu_score += points[i].score;
    }

    if (accu_score > 1e-7) {
        *score += accu_score;
        *radian = curr_radian;
    }
}



int main() {
    vector<Point> points;
    points.push_back(Point(1, 2, 1.2));
    points.push_back(Point(0, 0, 2.5));

    float radian = 0.0;
    float score = 0.0;
    maxScoreCircle(points, &radian, &score);
    cout << "Radian: " << radian << endl;
    cout << "Score: " << score << endl;

    return 0;
}
