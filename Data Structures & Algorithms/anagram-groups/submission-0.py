class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in map:
                map[sorted_s].append(s)
            else:
                map[sorted_s] = [s]
        
        return list(map.values())