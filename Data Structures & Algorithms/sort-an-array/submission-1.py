#going to implement mergesort as it achieves the minimal lowest bound bound time complexity by a comparitive sorting algorithm O(nlogn)
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        if l <= 1:
            return nums
        #if l%2 == 0: #even number length list
          #  i =  l//2 #mid point of the list
        #elif l%2 != 0: 
        i = (l//2)
        a = nums[:i]
        b = nums[i:]
        #print(a,b)
        asorted = self.sortArray(a)
        bsorted = self.sortArray(b)
        sortlist = self.merge(asorted,bsorted)
        return sortlist

    def merge(self, a, b):
        if a == None:
            return
        sortlist = []
        i, j = 0, 0
        while i <len(a) and j<len(b):
            if a[i] <= b[j]:
                sortlist.append(a[i])
                i += 1  
            else: 
                sortlist.append(b[j])
                j +=1
        if i == len(a):
            sortlist.extend(b[j:])
        elif j == len(b):
            sortlist.extend(a[i:])
        return sortlist 


        
        