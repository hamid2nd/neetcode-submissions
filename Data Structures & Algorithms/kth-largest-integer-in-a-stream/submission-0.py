import heapq

# ALGORITHM: keep a MIN heap holding only the k largest values seen so far.
# The smallest of those k values sits at the root, and it is exactly the
# k-th largest overall. On each add: push the new value; if the heap now
# has more than k values, pop the smallest (it can never be in the top k
# again). The answer is then just the root, heap[0].

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums              # store the list as an attribute
        heapq.heapify(self.heap)      # turn it into a min heap IN PLACE, O(n)
        while len(self.heap) > k:     # trim down to the k largest values
            heapq.heappop(self.heap)  # removes the smallest each time

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)    # add the new value, O(log k)
        if len(self.heap) > self.k:       # one too many: evict the smallest
            heapq.heappop(self.heap)
        return self.heap[0]               # root = smallest of the top k = k-th largest


# ------------------------------------------------------------
# WHY A MIN HEAP (not max)
# - We want to throw away small values cheaply. A min heap keeps the
#   smallest of our k values at the root, so the eviction candidate is
#   always one pop away, and that same root is the answer.
# - A value smaller than the root can never be in the top k, so it gets
#   pushed and immediately popped straight back out.
#
# COMPLEXITY
# - __init__: O(n) to heapify, plus O((n - k) log n) to trim.
# - add:      O(log k). The heap never exceeds k + 1 elements, however
#             long the stream gets. (My max-heap version was O(n) per add.)
#
# SYNTAX NOTES (mistakes in my first attempt)
# 1. heapq.heapify(list) works IN PLACE and returns None. Never write
#    x = heapq.heapify(...). Call it, then use the list itself.
# 2. heapq.heappush(heap, item) needs the heap as its first argument,
#    and also returns None. No assignment.
# 3. heapq.heappop(heap) removes AND returns the smallest item.
# 4. heap[0] PEEKS at the smallest item without removing it, O(1).
# 5. maxheap = self.maxheap is an alias, not a copy. Popping from it
#    would have emptied the real heap. A copy is self.maxheap.copy().
# 6. Can't negate a list: -heappop(h) is fine (negates the popped
#    value), heappop(-h) is an error.
# 7. range(k - 1) runs k - 1 times. range(k) runs k times.
# ------------------------------------------------------------



        
        
        
