class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # sort to avoid duplicates
        n = len(nums)

        # fix one number
        for i in range(n):
            # skip duplicate
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # two pointers
            l, r = i+1, n-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                # add result
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip duplicates
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        
        return res