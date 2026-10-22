class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n = len(s1)
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        for i in range(n):
            counter1[s1[i]] += 1
            counter2[s2[i]] += 1

        if counter1 == counter2:
                return True
        
        i = 0
        # sliding window with fixed window size = len(s1)
        for j in range(n, len(s2)):
            counter2[s2[j]] += 1
            counter2[s2[i]] -= 1
            if counter2[s2[i]] == 0:
                del counter2[s2[i]]
            i += 1
            
            if counter1 == counter2:
                return True
            
        
        return False
            
