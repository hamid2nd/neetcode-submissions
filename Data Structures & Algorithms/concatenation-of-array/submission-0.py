class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        twon = n*2
        ans = [0]*twon
        for i in range(n):
            ans[i] = nums[i]
        for i in range (n):
            ans[n+i] = nums[i]
        return ans