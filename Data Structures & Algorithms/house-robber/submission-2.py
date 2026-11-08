class Solution:
    def rob(self, nums: List[int]) -> int:
#want max combination of elements while obeying picking constraint (none can be next to eachother)
#brute force would be to calculate every possible valid collection in array, and then return the highest.
#highest sum hypothesis: as we loop through this list and check, we have things we keep, the highest  sum so far, and the highest possible sum we can add to the current index. These two lists can be the same, or different. e.g. in example 1, for index 2 and 3 the highest possible sum we can add is 1. For example 2, the high possible sum to add for index 2 (element 8) is 2, whereas for index 3 (element 3) is 9, whereas for index 4 is 10. 
#so need to code this algo.
        bestsum = [0,0] 
        for i in range(len(nums)):
            #newsum = bestsum[len(bestsum)-2] + nums[i]
            lastentry = bestsum.pop()
            newsum = max(bestsum) + nums[i]
            bestsum.append(lastentry)
            bestsum.append(newsum)
        return max(bestsum)
            #at each index, need to know the best potential sum we can make with this one, and if it is higher than the best right now.

#edge case is if we have >= 2 elements in the list