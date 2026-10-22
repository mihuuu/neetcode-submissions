class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        base = defaultdict(int)
        for c in t:
            base[c] += 1
        
        i = 0
        res = ""
        minLen = float('inf')
        counter = defaultdict(int)
        match, need = 0, len(base)
        for j in range(len(s)):
            counter[s[j]] += 1
            if counter[s[j]] == base[s[j]]:
                match += 1
            # valid substr
            while match == need:
                # update result
                if j-i+1 < minLen:
                    minLen = j-i+1
                    res = s[i:j+1]
                # shrink window
                counter[s[i]] -= 1
                if counter[s[i]] < base[s[i]]:
                    match -= 1
                i += 1
            
        if minLen != float('inf'):
            return res
        else:
             return ""

