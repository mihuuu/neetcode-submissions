class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding window
        i, j = 0, 0
        res = 0
        seen = set()
        while j < len(s):
            # shrink window from left (remove dup)
            if s[j] in seen:
                seen.remove(s[i])
                i += 1
            # expand window to right
            else:
                res = max(res, j-i+1)
                seen.add(s[j])
                j += 1
        return res