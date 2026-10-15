class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        # sort numbers by frequence, descending
        sorted_list = sorted(count.items(), key=lambda x: x[1], reverse=True)

        # get top k
        res = []
        for i in range(k):
            res.append(sorted_list[i][0])

        return res