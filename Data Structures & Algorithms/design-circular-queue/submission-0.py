# ============================================================
# LeetCode 622: Design Circular Queue (ring buffer) 
#I HAVE WRITTEN MY NOTES ON THE QUEUE IDEA/SYNTAX I DIDN'T KNOW OR MADE AN ERROR ON
# ============================================================
#
# THE % (MODULO) OPERATOR
#   a % b gives the REMAINDER when a is divided by b.
#     7 % 5 = 2      (7 = 1*5 + 2)
#     5 % 5 = 0      (5 = 1*5 + 0)
#     3 % 5 = 3      (3 is less than 5, so nothing to take away)
#    -1 % 5 = 4      (Python always gives a result between 0 and b-1)
#
#   Why it's useful here: index % k always lands in 0 .. k-1, so any
#   index that runs past the end of the array WRAPS back to the start.
#   With k = 5: index 4 -> (4+1) % 5 = 0. Like a clock going 12 -> 1.
#   Going backwards also wraps: (0-1) % 5 = 4 (needed for the deque, LC 641).
#
# DESIGN: store the FRONT index and the SIZE, and compute the rear from them.
#   - size tells empty (0) and full (k) apart. Comparing front and rear
#     can't do this, because they're in the same position in BOTH cases.
#   - "Removing" an element only moves the front index (logical removal);
#     old values stay in the array until they're overwritten.
#
# COMPLEXITY: every operation is O(1); space is O(k).
# ============================================================


class MyCircularQueue:

    def __init__(self, k: int):
        # Everything the methods share must be stored as self.<name>.
        # MY MISTAKE: wrote `frontindex = 0` without self. That creates a
        # local variable that disappears when __init__ ends.
        # MY MISTAKE: never stored k, so isFull couldn't see it.
        self.q = [0] * k      # fixed array of k slots, allocated once
                              # ([0] * k repeats the list k times: [0, 0, ..., 0])
                              # The zeros are placeholders; "empty" is decided by size.
        self.k = k            # capacity
        self.head = 0         # index of the front element
        self.size = 0         # number of elements currently in the queue
        # Named head, not front, to avoid confusion with the method Front().

    def enQueue(self, value: int) -> bool:
        # Add a value at the back. Return True if it worked, False if full.
        # MY MISTAKE: wrote `self.isFull == True`. Without (), that compares
        # the METHOD ITSELF to True, which is always False, so the check never
        # triggered. Methods must be CALLED with (). `== True` is unnecessary.
        if self.isFull():
            return False      # MY MISTAKE: printed instead of returning False.
                              # LeetCode checks return values; prints don't count.

        # The first free slot is `size` places after the front, wrapping round.
        # MY MISTAKE: had no % and never advanced the rear, so indices would
        # run off the end of the array.
        rear = (self.head + self.size) % self.k
        self.q[rear] = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        # Remove the front value. Return True if it worked, False if empty.
        if self.isEmpty():
            return False

        # Logical removal: move the front forward one slot (wrapping round)
        # and shrink the size. The old value stays in the array until it's
        # overwritten.
        # MY MISTAKE: `frontindex += 1` had no self. and no %, and the method
        # never returned True on success.
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True

    def Front(self) -> int:
        # Return the front VALUE, or -1 if empty (as the problem specifies).
        # MY MISTAKE: returned the index instead of the value at that index.
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self) -> int:
        # Return the back VALUE, or -1 if empty.
        # The last occupied slot is size-1 places after the front, wrapping round.
        # MY MISTAKE: returned an index, and the rear was never kept up to date.
        if self.isEmpty():
            return -1
        return self.q[(self.head + self.size - 1) % self.k]

    def isEmpty(self) -> bool:
        # MY MISTAKE: checked whether front == rear, which is ALSO true when
        # the queue is full. Also never returned anything (so it gave None),
        # and called self.front(), which doesn't exist: Python is
        # case-sensitive, so front() and Front() are different names.
        return self.size == 0

    def isFull(self) -> bool:
        # MY MISTAKE: tried to compute this from front - rear, which can't
        # tell empty from full, and used k without storing it as self.k.
        return self.size == self.k


# OTHER MISTAKE: indentation in enQueue was inconsistent (the if and else
# were indented differently), which is a syntax error in Python.
# Everything inside a block must be indented by exactly the same amount.
#
# TAKEAWAY: if a method is getting complicated, you're probably missing a
# piece of state. Adding `size` made isEmpty and isFull one line each.


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()