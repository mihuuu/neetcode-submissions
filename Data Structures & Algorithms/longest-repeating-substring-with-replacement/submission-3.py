class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # replace with the most frequent char
        # replacement num = substr length - max frequency
        # valid if replacement <= k
        counter = defaultdict(int)
        i, j = 0, 0
        res = 0
        maxCount = 0
        for j in range(len(s)):
            counter[s[j]] += 1
            maxCount = max(maxCount, counter[s[j]])
            replaceNum = (j-i+1) - maxCount
            # shrink window if can't replace within k
            if replaceNum > k:
                counter[s[i]] -= 1
                i += 1
            # expand window
            res = max(res, j-i+1)
        return res

