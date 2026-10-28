class Solution:
    def findMin(self, nums: List[int]) -> int:
        i, j = 0, len(nums)-1
        # min element is the first of right part 
        while i < j:
            mid = (i + j) // 2
            # compare mid with the right value
            # min is in the left part (including mid)
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1
        
        return nums[i]