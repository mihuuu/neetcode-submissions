class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        max = 1
        zero_cnt = 0
        for n in nums:
            if n != 0:
                max *= n
            else:
                zero_cnt += 1
        
        res = [0] * len(nums)
        if zero_cnt > 1:
            return res

        for i, n in enumerate(nums):
            if zero_cnt > 0:
                # has one zero
                res[i] = 0 if n else max
            else:
                # no zero, can use division
                res[i] = max // n

        return res