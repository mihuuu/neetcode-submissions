class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # (j-i) * min(heights[i], heights[j])
        i = 0
        j = len(heights) - 1
        maxArea = 0
        while i < j:
            area = (j-i) * min(heights[i], heights[j])
            maxArea = max(maxArea, area)
            # greedy: move the pointer with smaller height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea