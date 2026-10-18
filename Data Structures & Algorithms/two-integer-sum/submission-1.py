# ALGORITHM (complement lookup, two passes):
# For any pair that sums to target, nums[i] + nums[j] = target, so
# nums[j] = target - nums[i]. In other words, nums[j] is the "complement"
# of nums[i].
#
# Pass 1: build a hash map from each number's COMPLEMENT to that number's
#         INDEX:  complement_index[target - nums[i]] = i.
#         (A set only remembers values; the dict also remembers WHERE each
#         complement came from, which is how we get the indices back.)
# Pass 2: for each j, check whether nums[j] is someone's complement.
#         If it is, and that someone isn't j itself (a number can't pair
#         with itself), we've found the pair.
#
# Complexity: O(n) time (two passes, each O(1) per element thanks to the
# hash map), O(n) space for the dict. Brute force (checking every pair)
# would be O(n^2).
#
# Duplicates, e.g. nums = [3, 3], target = 6: both 3s give complement 3, so
# the dict keeps only the LAST index, {3: 1}. At j = 0 we find index 1 != 0,
# so it still returns a valid pair [1, 0].
#
# ------------------------------------------------------------
# 2ND ATTEMPT: do it in ONE pass (the standard solution)
# ------------------------------------------------------------
# Instead of building the whole dict first, build it AS YOU GO:
#   1. Start with an empty dict mapping value -> index ("numbers seen so far").
#   2. Loop through nums once with enumerate, getting index i and value x.
#   3. FIRST, check whether target - x is already in the dict.
#      If yes, its partner appeared earlier: return [dict[target - x], i].
#   4. ONLY THEN add x to the dict: dict[x] = i.
# Because you check BEFORE adding the current number, it can never match
# itself, so the i != j check disappears. It's also faster in practice:
# it stops as soon as the pair is found (same idea as the early-exit
# version of Contains Duplicate). Aim for about 5 lines.
# ------------------------------------------------------------

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Pass 1: complement -> index of the number it came from
        complement_index = {target - x: i for i, x in enumerate(nums)}
        # ------------------------------------------------------------
        # WHAT THIS LINE DOES (a "dict comprehension"):
        #
        # It is exactly the same as this loop:
        #     complement_index = {}
        #     for i, x in enumerate(nums):
        #         complement_index[target - x] = i
        #
        # Reading it piece by piece:
        #   enumerate(nums)       -> gives (index, value) pairs:
        #                            (0, nums[0]), (1, nums[1]), ...
        #   for i, x in ...       -> unpacks each pair: i = index, x = value
        #   target - x : i        -> store the KEY target - x (the complement
        #                            this number needs) with the VALUE i
        #                            (where this number is in the list)
        #   { ... }               -> collect all of those into one dict
        #
        # Example: nums = [2, 7, 11, 15], target = 9
        #   i=0, x=2  -> key 9-2=7,   value 0
        #   i=1, x=7  -> key 9-7=2,   value 1
        #   i=2, x=11 -> key 9-11=-2, value 2
        #   i=3, x=15 -> key 9-15=-6, value 3
        #   complement_index = {7: 0, 2: 1, -2: 2, -6: 3}
        #
        # Meaning: "the number at index 0 needs a 7", "the number at
        # index 1 needs a 2", and so on. In pass 2, if we meet a 7, we
        # look up complement_index[7] = 0 and know its partner is index 0.
        #
        # Why NOT just enumerate(nums) on its own: dict(enumerate(nums))
        # maps index -> value, which the list already does. We need
        # (something we can look up) -> index, and the comprehension
        # lets us choose both the key and the value.
        #
        # Duplicate keys: if two numbers need the same complement, the
        # later index overwrites the earlier one (a key appears once).
        # ------------------------------------------------------------

        # Pass 2: is nums[j] the complement of some OTHER element?
        for j in range(len(nums)):
            if nums[j] in complement_index:          # O(1) lookup
                i = complement_index[nums[j]]        # index of its partner
                if i != j:                           # can't use the same element twice
                    return [j, i]
