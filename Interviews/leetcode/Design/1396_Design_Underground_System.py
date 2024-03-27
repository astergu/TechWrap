'''
An underground railway system is keeping track of customer travel times between different stations. They are using this data to calculate the average time it takes to travel from one station to another.

Implement the UndergroundSystem class:

    void checkIn(int id, string stationName, int t)
        A customer with a card ID equal to id, checks in at the station stationName at time t.
        A customer can only be checked into one place at a time.
    void checkOut(int id, string stationName, int t)
        A customer with a card ID equal to id, checks out from the station stationName at time t.
    double getAverageTime(string startStation, string endStation)
        Returns the average time it takes to travel from startStation to endStation.
        The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
        The time it takes to travel from startStation to endStation may be different from the time it takes to travel from endStation to startStation.
        There will be at least one customer that has traveled from startStation to endStation before getAverageTime is called.

You may assume all calls to the checkIn and checkOut methods are consistent. If a customer checks in at time t1 then checks out at time t2, then t1 < t2. All events happen in chronological order.
'''

from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.station_checks = defaultdict(tuple)
        self.time = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.station_checks[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        s_time, s_station = self.station_checks[id]
        total = t - s_time
        self.time[(s_station, stationName)].append(total)        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return sum(self.time[(startStation, endStation)]) / len(self.time[(startStation, endStation)])        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
    
if __name__ == '__main__':
    us = UndergroundSystem()
    us.checkIn(45, "Leyton", 3)
    us.checkIn(32, "Paradise", 8)
    us.checkOut(27, "Leyton", 10)