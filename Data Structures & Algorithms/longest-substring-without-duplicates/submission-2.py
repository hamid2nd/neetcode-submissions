#brute force: loop through the array; store current substring in array, check every letter of the current substring against the current array character, if it doesn't match any then add it to the current substring (and its length) and continue, if it does then store the current substring and start another one.  
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0 #length of the longest string we have found so far
        currentlong = 0 #length of the current substring    
        currstring =[] #array that will store the current string characters as seperate entries
        for character in s: 
            for duplicate in range(len(currstring)):
                if currstring[duplicate] == character: 
                    currstring = currstring[duplicate + 1:] # drop everything up to and including the earlier copy, keep the chars after it
                    currentlong = len(currstring) # length of what's left, before we add the current character
                    break 
            currstring.append(character)
            #print (currstring)
            currentlong += 1
            if currentlong > longest: 
                longest = currentlong 
        return longest
                         