class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        edgetovcount = [0]*n
        trustees = set() #tracking all trustees as a judge cannot be a trustee
        for i in range(len(trust)):
            edgetovcount[trust[i][1]-1] += 1
            trustees.add(trust[i][0]) 
            
        for i in range(len(edgetovcount)):
            if edgetovcount[i] == n-1: #this entry is a potential judge
                potjudge = i+1
                x = potjudge in trustees
                if x == False: 
                    return potjudge
        return -1 


