class Solution:

    def encode(self, strs: List[str]) -> str:
        # each stores len#str
        res = []
        for s in strs:
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i, j = 0, 0
        while j < len(s):
            if s[j] == '#':
                length = int(s[i:j])
                res.append(s[j+1:j+length+1])
                i = j + length + 1
                j = i
            else:
                j += 1
        
        return res
