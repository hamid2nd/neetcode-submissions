class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = [] #stack
        end = -1 #pointer to the last element added to the stack. Starts at -1, becomes 0 when something is in the stack etc. 
        for i in operations: 
            if i == '+':
                if end >= 1: #ensure stack has at least 2 items to add
                    newrecord = record[end] + record[end-1] 
                    record.append(newrecord)
                    end += 1
            elif i == 'D':
                if end > -1: #ensure the stack has at least one item to double
                    newrecord = 2 * record[end]
                    record.append(newrecord)
                    end += 1
            elif i == 'C':
                if end > -1: #ensure the stack has at least one item to remove
                    record.pop()
                    end -= 1
            else: #must be a score to append
                i = int(i)
                record.append(i)
                end +=1
        return sum(record) #built in python function to get the sum of the array
