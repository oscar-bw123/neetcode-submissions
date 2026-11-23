class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict = {}

        for char in s:
            if char in dict:
                dict[char] += 1
            else: 
                dict[char] = 1

        for char in t:
            if char in dict:
                if dict[char] > 1:
                    dict[char] -= 1
                else:
                    dict.pop(char)

        if len(dict) == 0:
            return True
        else: return False
            
        