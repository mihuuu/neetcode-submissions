class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Min Heap
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        
        # heap size = k, stores (freq, num) pair
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            # remove the smallest one
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [item[1] for item in heap]
        
