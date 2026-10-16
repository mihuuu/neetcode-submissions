class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # hint: how to find the start of a sequence?
        # check n-1 (if n-1 is not included, n,n+1,... sequence)
        s = set(nums)
        res = 0
        
        for num in s:
            if (num - 1) not in s:
                # num is the start of seq
                cur = num
                count = 0
                while cur in s:
                    cur += 1
                    count += 1
                res = max(res, count)
        
        return res
