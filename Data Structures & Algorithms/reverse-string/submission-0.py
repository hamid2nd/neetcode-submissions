class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        length = len(s)
        end = length -1 #index/pointer to the end of the list
        start = 0 #index pointing at start of the list
        steps = length//2 #gives lower of division result, so e.g. list of length 5 gives us 2 steps (swaps), the middle value isn't touched
        for i in range(steps):
            startval = s[start]
            endval = s[end]
            s[start] = endval
            s[end] = startval #swapping the start and end values of the list
            end -= 1
            start += 1 #moving start index forward one spot, end index back one spot

        