class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i, j = 0, len(nums)-1
        # two sorted array, find the pivot (min element)
        while i < j:
            mid = (i + j) // 2
            # compare mid with the right value
            # min is in the left part (including mid)
            if nums[mid] < nums[j]:
                j = mid
            else:
                i = mid + 1
        
        # pivot index = i
        pivot = i
        # choose one part to binary search
        if target >= nums[pivot] and target <= nums[-1]:
            i, j = pivot, len(nums)-1
        else:
            i, j = 0, pivot-1

        while i <= j:
            mid = (i + j) // 2
            if nums[mid] < target:
                i = mid + 1
            elif nums[mid] > target:
                j = mid - 1
            else:
                return mid
        
        return -1
            