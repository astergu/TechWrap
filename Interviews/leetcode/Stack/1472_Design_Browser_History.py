'''
You have a browser of one tab where you start on the homepage and you can visit another url, get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

    BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
    void visit(string url) Visits url from the current page. It clears up all the forward history.
    string back(int steps) Move steps back in history. If you can only return x steps in the history and steps > x, you will return only x steps. Return the current url after moving back in history at most steps.
    string forward(int steps) Move steps forward in history. If you can only forward x steps in the history and steps > x, you will forward only x steps. Return the current url after forwarding in history at most steps.

'''

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0

    def visit(self, url: str) -> None:
        for i in range(len(self.history) - 1, self.curr, -1):
            self.history.pop()
        self.history.append(url)
        self.curr += 1

    def back(self, steps: int) -> str:
        while steps and self.curr > 0:
            steps -= 1
            self.curr -= 1
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        while steps and self.curr < len(self.history) - 1:
            steps -= 1
            self.curr += 1
        return self.history[self.curr]



if __name__ == '__main__':
    bh = BrowserHistory("leetcode.com")
    bh.visit("google.com")       # You are in "leetcode.com". Visit "google.com"
    bh.visit("facebook.com")     # You are in "google.com". Visit "facebook.com"
    bh.visit("youtube.com")      # You are in "facebook.com". Visit "youtube.com"
    print(bh.back(1))                   # You are in "youtube.com", move back to "facebook.com" return "facebook.com"
    print(bh.back(1))                  # You are in "facebook.com", move back to "google.com" return "google.com"
    print(bh.forward(1))                # You are in "google.com", move forward to "facebook.com" return "facebook.com"
    bh.visit("linkedin.com")     # You are in "facebook.com". Visit "linkedin.com"
    print(bh.forward(2))                # You are in "linkedin.com", you cannot move forward any steps.
    print(bh.back(2))                   # You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
    print(bh.back(7))                   # You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"