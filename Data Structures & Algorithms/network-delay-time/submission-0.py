import heapq
from collections import defaultdict  #Claude (fix 4): needed to build the adjacency list

# ============================================================
#Claude: MY MAIN LOGIC ERROR - THE STALE CHECK (revise this!)
# ------------------------------------------------------------
# I only explored a popped node "if short[node] > popped distance".
# But every time I push (distance, node), I've ALREADY written that same
# distance into short. So when it's popped, the two are EQUAL, the
# condition is False, and the node's edges are never explored.
#
# The correct logic is the opposite: the heap can hold OLD entries for a
# node (pushed before a shorter route was found). When popped:
#   - if popped distance > short[node]: it's STALE (a shorter route was
#     found later), so SKIP it with continue
#   - otherwise: it's the current best, so the node is now SETTLED
#     (its distance is final) and I explore its edges
# short is updated when PUSHING (in the relaxation), never when popping.
# ============================================================

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        short = {} #hash map with key being node, and value being shortest distance to that note from the source. This is not the final distances until node is added to closed below
        heap =[]
        heapq.heapify(heap) #making heap to store entries of nodes and their distance to source node

        #Claude (fix 4): build an adjacency list ONCE: node -> list of (neighbour, weight).
        # Before, every pop scanned ALL of times (O(V*E)); now each node only
        # looks at its own edges. Also fixes syntax issue 5 (unpack each edge
        # with "for u, v, w in times" instead of indexing times[i]).
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        for i in range(n):
            short[i+1] = float('inf') #everything is infinite distance at the start
            #Claude (fix 3): float('inf') instead of the string "inf"; comparing a
            # number with a string crashes in Python 3.
            #Claude (extra fix): I had "if i != k", but i runs 0..n-1 while nodes are
            # 1..n, so it skipped node k+1 instead of k. Now all nodes start at inf...
        short[k] = 0  #Claude (fix 2): ...and the source is set to 0 explicitly

        #Claude (fix 2): removed pre-loading the source's direct neighbours and
        # pushing every node at the start. Only the source goes in; the main loop
        # discovers its neighbours the first time it pops k.
        # (This also removed the "heapq.heappush = [...]" line, syntax issue 7: that
        # OVERWROTE the heappush function instead of calling it.)
        heapq.heappush(heap, (0, k)) #adding initial current node and distance to it to the heap

        while heap: #this runs until the heap is empty
            nearestnode = heapq.heappop(heap) #this is the nearest node
            #Claude (fix 1): stale check (see top comment). Skip OLD entries;
            # otherwise this node is now settled, so explore its edges.
            if nearestnode[0] > short[nearestnode[1]]:
                continue
            for v, w in graph[nearestnode[1]]:  #Claude (fix 4 + 5): this node's own edges only
                #now going to check if we need to update nodes reachable from this one as the path to them is now shorter
                potshorter = nearestnode[0] + w
                if potshorter < short[v]: #checking if updatedpath through this node is shorter than whatever we have now 
                    short[v] = potshorter
                    heapq.heappush(heap, (potshorter, v)) #new shortest distance to node is pushed to the heap

        largest = max(short.values())
        #Claude: I originally got the max by pushing every distance into a max heap
        # and popping it. max() does it in one line (and in O(n), versus O(n log n)
        # for pushing everything into a heap).
        if largest == float('inf'):  #if any node is unreachable, the largest distance is inf
            return -1
        return largest

        


