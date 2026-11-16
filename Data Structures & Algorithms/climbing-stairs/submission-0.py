# Algo: x is the number of 1-steps in a way, y is the number of 2-steps. x + 2y = n.
# y can be anything from 0 up to n // 2 (floor div), and each y fixes x = n - 2y.
# So there are n // 2 + 1 (x, y) combos, ORDER INDIFFERENT.
# To account for order: each combo has x + y steps in total. (x + y)! would count orderings
# as if every step were different, but swapping two 1-steps (or two 2-steps) gives the SAME
# climb, e.g. 1,1,2 with the 1s swapped is still 1,1,2. So divide out those swaps:
# (x + y)! / (x! * y!) = math.comb(x + y, y), i.e. choose which positions are the 2-steps.
# Answer = sum of math.comb(x + y, y) over every y. Works for odd and even n alike.
#
# Alternative (the intended NeetCode solution), dynamic programming (DP): build the answer up
# from smaller versions of the same problem, storing each small answer so it's never redone.
# The last move onto step n was either a 1-step from n - 1 or a 2-step from n - 2, so
# ways(n) = ways(n - 1) + ways(n - 2), with ways(0) = ways(1) = 1. Building up from the bottom:
# 1, 1, 2, 3, 5, 8, ... (Fibonacci), keeping only the last two values, gives O(n) time, O(1) space:
#     one, two = 1, 1
#     for _ in range(n - 1):
#         one, two = one + two, one
#     return one
import math
class Solution:
    def climbStairs(self, n: int) -> int:
        noways = 0                        # number of ways of taking steps
        for twos in range(n // 2 + 1):    # every possible number of 2-steps, including 0
            ones = n - 2 * twos           # the rest of the climb is 1-steps
            noways += math.comb(ones + twos, twos)   # distinct orderings of this combo
        return noways
               
        