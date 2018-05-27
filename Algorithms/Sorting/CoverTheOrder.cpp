/**
 * Air traffic control of one country wants to check how well its radars are covering the border. There are plenty of radars each covering one contiguous strip of the border. Some radars' coverage strips overlap. Because of the numerous overlaps it is hard for the air traffic control managers to compute the exact length of the border that is covered. This will be your task.

The strip is represented as a line, which is L meters long.

For each radar we know the left and right end of its coverage strip relative to the left end of the border. Hence, all such coverage strips will begin and end somewhere in the range [0, L], which means they fall completely within the border. They will also have an integer length of at least 1.

You will have to write a function, which receives as arguments L and a list of pairs of integers - the radar coverage strips ends. Your function must return one integer - the total area of the border that is covered by at least one radar, in meters.

You can assume that 1 <= L <= 10^9 and there will be no more than 1,000 radars.

SAMPLE INPUT

L = 100
radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]

SAMPLE OUTPUT

77

In the sample input the border is 100 meters long and there are 5 radars covering parts of it. Effectively there are three areas of the border that are completely covered by at least one radar:

    3 to 25, which includes in itself the area between 5 and 10 covered by another radar
    39 to 40, which is covered by a single radar
    45 to 99, which is the combined coverage of two radars with coverage [45, 50] and [46, 99]
 *
 *
 */

#include <vector>
#include <algorithm>

using namespace std;

int cover_the_border(int l, const vector< pair<int, int> >& radars) {
    // Example arguments:
    // l = 100
    // radars = [ [5, 10], [3, 25], [46, 99], [39, 40], [45, 50] ]
}

