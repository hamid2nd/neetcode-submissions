import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = [-n for n in stones]
        heapq.heapify(max_heap)
        while len(max_heap) > 1: 
            x = -heapq.heappop(max_heap)
            y = -heapq.heappop(max_heap)
#as x is removed first from a max heap, it must either be the heavier stone or equal to y's weight, so only need to check if x is bigger to then add back the remaining weight to heap
            if x > y: 
                x = x - y
                heapq.heappush(max_heap,-x)
            
        return -max_heap[0] if max_heap else 0
        #^this last line returns max heap if it exists (so one element left after while loop), if it doesn't exist it returns 0 
         