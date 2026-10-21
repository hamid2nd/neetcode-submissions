class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
# One-dictionary approach, O(m*n) for m words of length up to n:
# Instead of comparing every word with every other word (O(m^2)), work out a "letter
# signature" for each word: a tuple of 26 counts, one for each letter a-z.
# Anagrams have exactly the same signature, so use it as a dictionary KEY, with the
# list of words that share it as the VALUE. Each word does one O(1) lookup to find its
# group, so no duplicate groups get made. A tuple is used because dict keys must be
# hashable (unchangeable), and lists aren't.
        groups = {}                                  # signature -> list of words with that signature
        for i in range(len(strs)):
            letters = self.chcheck(strs[i])
            if letters not in groups:                # first word with this signature: start a new group
                groups[letters] = []
            groups[letters].append(strs[i])          # add the word to its group
        return list(groups.values())                 # each value is one group of anagrams

        
    def chcheck(self, word):
        letters = [0] * 26                           # one count per letter, a-z
        for ch in word:
            letters[ord(ch) - ord('a')] += 1         # 'a' -> index 0, 'z' -> index 25
        return tuple(letters)                        # tuple so it can be a dict key