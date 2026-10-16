class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        res = 1
        count = 1
        
        pre = nums[0]
        i = 1

        while i < len(nums):
            if nums[i] == pre:
                i += 1
                continue
            if nums[i] - pre == 1:
                count += 1
                res = max(res, count)
            # reset
            else:
                count = 1
            pre = nums[i]
        
        return res