'''
Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).

All messages will come in chronological order. Several messages may arrive at the same timestamp.

Implement the Logger class:

    Logger() Initializes the logger object.
    bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
'''

class Logger:
    def __init__(self):
        self.history = dict()
    
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.history or timestamp - self.history[message] >= 10:
            self.history[message] = timestamp
            return True
        return False


if __name__ == '__main__':
    logger = Logger()
    # logging string "foo" at timestamp 1
    print(logger.shouldPrintMessage(1, "foo")) # returns true
    #logging string "bar" at timestamp 2
    print(logger.shouldPrintMessage(2,"bar")) # returns true
    # logging string "foo" at timestamp 3
    print(logger.shouldPrintMessage(3,"foo")) # returns false
    # logging string "bar" at timestamp 8
    print(logger.shouldPrintMessage(8,"bar")) # returns false
    # logging string "foo" at timestamp 10
    print(logger.shouldPrintMessage(10,"foo")) # returns false
    # logging string "foo" at timestamp 11
    print(logger.shouldPrintMessage(11,"foo")) # returns true