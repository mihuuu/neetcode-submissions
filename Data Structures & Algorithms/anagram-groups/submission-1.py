class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        map = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss in map:
                map[ss].append(s)
            else:
                map[ss] = [s]
        
        for list in map.values():
            res.append(list)
        return res
