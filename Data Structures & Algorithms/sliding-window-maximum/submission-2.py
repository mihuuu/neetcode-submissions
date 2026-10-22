class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonic deque (keep decreasing order)
        # deque: doubly-linked list, better than pop(0)
        # keep max element at the front of deque
        res = []
        q = deque()
        for i in range(len(nums)):
            # remove elements smaller than current value
            # to maintain a decreasing queue
            while q and q[-1] < nums[i]:
                q.pop()
            q.append(nums[i])

            # remove max element if outside window
            if i >= k and nums[i-k] == q[0]:
                q.popleft() # O(1)

            if i >= k-1:
                res.append(q[0])
        
        return res
            
