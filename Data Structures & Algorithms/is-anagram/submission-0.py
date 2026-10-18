# ALGORITHM: use a hash map (dict) as a COUNTER, the same idea as the count
# array in counting sort, but with the letters themselves as keys instead of
# indexes 0..k-1. Count up every letter in s, then count down every letter
# in t. If t ever has more of a letter than s (a count goes below 0), they
# aren't anagrams.
#
# Why no final "are all counts 0?" check: the lengths are equal, so if no
# count ever went negative, every count must end at exactly 0.
#
# Complexity: O(n) time (one pass over each string), O(1) extra space
# (at most 26 keys for lowercase letters).
# One-line alternative: return Counter(s) == Counter(t)  (from collections)

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):                     # different lengths can't be anagrams
            return False
        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1   # add one for each letter in s
        for ch in t:
            counts[ch] = counts.get(ch, 0) - 1   # take one away for each letter in t
            if counts[ch] < 0:                   # t has more of this letter than s
                return False
        return True
        