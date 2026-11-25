class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t): return False

        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else: dict[char] = 1
        
        for char in t:
            if char in dict:
                if dict[char] == 0:
                    return False
                else: dict[char] -=1
            else:
                return False

        return True