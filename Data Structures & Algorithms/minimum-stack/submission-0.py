# Algorithm: keep a second stack, minstack, alongside the main one.
# minstack[i] holds the minimum of everything in stack[0..i], so the top of
# minstack is always the minimum of the whole current stack.
# On push: add val to stack, then push min(val, current min) onto minstack.
# On pop: pop from both stacks together. That uncovers the previous minimum
# automatically, because minstack remembers what the min was before each push.
# Every operation is O(1).

class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []   # minstack[-1] is always the current minimum

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minstack) > 0:   # stack already had values pushed to it
            self.minstack.append(min(val, self.minstack[-1]))
        else:
            self.minstack.append(val)   # empty, so new value automatically minimum

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()   # keep both stacks the same length

    def top(self) -> int:
        return self.stack[-1]   # peek without popping and re-appending

    def getMin(self) -> int:
        return self.minstack[-1]
