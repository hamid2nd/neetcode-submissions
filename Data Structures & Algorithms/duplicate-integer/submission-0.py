#Algorithm is very simple: Turn the list into a set. As a set cannot have duplicates, it won't add duplicate numbers.This means if the len(set) created from the list is smaller than the list then the list must have duplicates.
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nodupli = set(nums)
        if len(nodupli) < len(nums):
            return True #duplicates must exist
        else: 
            return False #duplicates do not exist 
        