from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        kcommonpairs = Counter(nums).most_common(k) #list of the k most common key value pairs, where the first element (of the first pair element) is the value from nums, and the second element (of the first pair element) is the frequency of that value from nums
        kcommonvalues = []
        for i in range(len(kcommonpairs)):
            kcommonvalues.append(kcommonpairs[i][0])
        return kcommonvalues