class Solution:
    def isPalindrome(self, s: str) -> bool:
        # two pointers
        i = 0
        j = len(s) - 1
        while i < j:
            if not self.isValid(s[i]):
                i += 1
                continue
            if not self.isValid(s[j]):
                j -= 1
                continue
            
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def isValid(self, c: str) -> bool:
        # Python allows implicit line continuation inside parentheses
        # or use \ to break lines
        # Simpler: 'A' <= c <= 'Z'
        return (
            ord('A') <= ord(c) <= ord('Z')
            or ord('a') <= ord(c) <= ord('z')
            or ord('0') <= ord(c) <= ord('9')
        )
