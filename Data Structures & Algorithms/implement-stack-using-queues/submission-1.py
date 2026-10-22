from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x) #same as stack, just add value to the back

    def pop(self) -> int:
        for x in range (len(self.q)-1): #shifting every element infront of top of the queue (stack) to be infront of it, so that when we pop we get the top value (the value that was top of the queue at the start of this operation)
            temp = self.q.popleft()
            self.q.append(temp)
        return self.q.popleft()

    def top(self) -> int:
        for x in range(len(self.q)-1): #same idea as above for popping, just not removing value this time (peeking)
            temp = self.q.popleft()
            self.q.append(temp)
        val = self.q.popleft()
        self.q.append(val) #adding the item back in at the end, list order restored
        return val

    def empty(self) -> bool:
        if len(self.q) == 0:
            return True
        else:
            return False  



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()