#outputting the biggest +ve difference between two elements in the array, where the second element comes after the first. If there is no +ve difference like this in the array then return zero
#Brute force: check every index to index (after it) difference in the array, return the largest +ve difference or 0 if there is no +ve difference. Really high complexity of n!.
#reducing complexity of the brute force: We can step through list once, keeping track of the lowest index we have passed and the highest index after it
#create hashmap called lowest. In it we store lowest and highest pairs - lowest vals are keys, initially 0 until we either find higher val to store as its val, or we find a new lowest to focus on. Have a variable called lowest which keeps track of the current lowest val. 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currlow = prices[0]
        highprofpair = {}
        highprofpair[currlow] = 0 #inital entry of lowest val (the first val in prices) as a key, with its val pair as 0 as we don't know the highest pair/if highest pair exists etc.
        for i in range(len(prices)):
            if prices[i] < currlow:
                currlow = prices[i]
                highprofpair[currlow] = 0
            elif prices[i] > currlow:
                if prices[i] > highprofpair[currlow]: #check if this value that is biggest than our current lowest value is also biggest than the biggest val we've found since the lowest
                    highprofpair[currlow] = prices[i]
        maxdiff = 0 #now seeing the max diff we have 
        for l, h in highprofpair.items():
            if h == 0:
                continue 
            else: 
                diff = h - l 
                if diff > maxdiff:
                    maxdiff = diff
        return maxdiff


        