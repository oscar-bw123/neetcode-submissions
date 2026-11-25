class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else: dict[char] = 1
        
        for char in t:
            if char in dict:
                if dict[char] > 1:
                    dict[char] -= 1
                else: dict.pop(char)
            else:
                dict[char] = 1

        if len(dict) == 0:
            return True
        else: return False