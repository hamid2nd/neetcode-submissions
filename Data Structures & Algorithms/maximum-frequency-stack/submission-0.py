class FreqStack:

    def __init__(self):
        self.stack = []
        self.freqcounter = {}
        self.output =[]
        return None 

    def push(self, val: int) -> None:
        self.stack.append(val)
        check = val in self.freqcounter
        if check == True:
            self.freqcounter[val] = self.freqcounter[val]+1
        else: 
            self.freqcounter[val] = 1
        return None 

    def pop(self) -> int:
        keymaxfreq, maxv = max(self.freqcounter.items(), key=lambda kv: kv[1])   #this gives us the max value in the hashmap, as well as the key that holds it
        #now just need to add the tie functionality
        ties =[] #list of stack entries that have the same frequency
        for i in self.freqcounter:
            if self.freqcounter[i] == maxv:
                ties.append(i)   # FIX: store the KEY, not its frequency
        if len(ties) == 1: #no tie 
            for i in range(len(self.stack)):
                if self.stack[len(self.stack)-1-i] == keymaxfreq: 
                    x = self.stack.pop(len(self.stack)-1-i)
                    self.freqcounter[keymaxfreq] -= 1
                    return x 
        if len(ties) > 1:
            bestpos = -1   # highest stack position of any tied key found so far
            for key in ties:
                found = -1 
                for y in range(len(self.stack)):
                    if self.stack[len(self.stack)-1-y] == key:   # scanning from the top down
                        found = len(self.stack)-1-y   # topmost position of this key
                        break                         # only need its topmost copy
                if found > bestpos:   # this key sits higher than the best so far
                    bestpos = found
            x = self.stack.pop(bestpos)
            self.freqcounter[x] -= 1
            return x



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()