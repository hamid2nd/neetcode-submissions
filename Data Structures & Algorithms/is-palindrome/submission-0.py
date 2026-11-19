class Solution:
    def isPalindrome(self, s: str) -> bool:
        frontp = 0
        backp = len(s) - 1
        while frontp < backp:
            #shift each pointer past non-alphanumeric characters
            while frontp < backp and not s[frontp].isalnum():
                frontp += 1
            while frontp < backp and not s[backp].isalnum():
                backp -= 1
            if s[frontp].lower() == s[backp].lower():   # ignore case: "A" matches "a"
                frontp +=1 
                backp -=1
            else: #not a palindrome
                return False
        return True
                
        