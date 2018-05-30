#include <vector>
using namespace std;

vector<double> getDigitsDecimal(const double inputTime) {
    vector<double> digits;
    double beforeDecimal = floor(inputTime);
    double afterDecimal = inputTime - beforeDecimal;
    digits.push_back(beforeDecimal);
    digits.push_back(afterDecimal);
    return digits;
}

double getRealTime(const double lidarTime, const double computerTime) {
    vector<double> digitsLidar = getDigitsDecimal(lidarTime);
    vector<double> digitsComputer = getDigitsDecimal(computerTime);
    double afterDecimalLidar = digitsLidar[1];
    if (fabs(digitsComputer[0] + afterDecimalLidar - computerTime) > 0.150) { 
        if (afterDecimalLidar < 0.150) {// real: 56.125, lidar: *.125, computer: 55.990
            return digitsComputer[0] + 1 + afterDecimalLidar; 
        }
        return digitsComputer[0] - 1 + afterDecimalLidar;  // real: 56.980, lidar: *.980, computer: 57.110
    } else {  
        return digitsComputer[0] + afterDecimalLidar;
    } 
}
