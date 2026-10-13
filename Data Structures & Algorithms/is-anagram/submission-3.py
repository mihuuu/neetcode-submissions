class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # attention!
        if len(s) != len(t):
            return False
    
        counter = dict()
        for i in s:
            counter[i] = counter.get(i, 0) + 1
        
        for i in t:
            if counter.get(i, 0) == 0:
                return False
            counter[i] -= 1
        
        return True
