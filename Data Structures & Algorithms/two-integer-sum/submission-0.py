class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i in range(len(nums)):
            pre = target - nums[i]
            if pre in map:
                return [map[pre], i]
            
            map[nums[i]] = i
        
        return []