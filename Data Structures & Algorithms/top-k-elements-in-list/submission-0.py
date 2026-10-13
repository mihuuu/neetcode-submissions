class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = dict(Counter(nums))
        s = sorted(count.items(), key=lambda x: x[1], reverse=True)
        return [x[0] for x in s[0:k]]