# I came up with "Go away" algorithm: walk through the array checking each element.
# If you find a 0, send it away to the start (delete it, insert a 0 at index 0).
# If you find a 2, send it away to the end (delete it, append a 2).
# 1s stay where they are, so they end up in the middle.
# Use a while loop rather than a for loop so we control when i moves forward,
# and stop once we reach the 2s we've already sent to the end.

#NOTE FOR WHEN DOING RE-DO: The best algorithm to solve this (which is O(n) time complexity compared to mine being O(n squared)) is: Keep three pointers (low and mid at the start, high at the end) and scan with mid: swap 0s back to low (advancing both low and mid), skip 1s (advancing mid), and swap 2s forward to high (moving high back but leaving mid in place so the swapped-in element gets checked).

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        end = len(nums)  # everything from index `end` onwards is a 2 we've already moved
        while i < end:
            if nums[i] == 0:
                del nums[i] 
                nums.insert(0, 0) #Asked Claude, found this syntax for inserting a value at a specific index into a list. So pushes every element forward once, puts this at 0 (first number is the index you are inserting at, 2nd is the value being inserted)
                i += 1  # the next unchecked element is still at i+1, so move on
            elif nums[i] == 2: 
                del nums[i]
                nums.append(2)
                end -= 1  # one more finished 2 at the end, so stop one earlier
                # don't increase i: the next element just slid back into index i
            else:
                i += 1  # it's a 1, leave it and move on