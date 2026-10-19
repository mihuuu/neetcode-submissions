class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Original: move left pointer one by one
        # Optimize: jump to the correct position without dup
        res = 0
        map = {} # num: index
        i, j = 0, 0
        while j < len(s):
            # shrink window from left
            if s[j] in map and map[s[j]] >= i:
                # jump to the next index of dup
                i = map[s[j]] + 1
            # expand window to right
            res = max(res, j-i+1)
            map[s[j]] = j
            j += 1
        
        return res
