class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ''
        for c in s:
            if self.isValid(c):
                s2 += c.lower()
        
        return s2 == s2[::-1] # compare reversed str

    def isValid(self, c: str) -> bool:
        check1 = ord(c) >= ord('A') and ord(c) <= ord('Z')
        check2 = ord(c) >= ord('a') and ord(c) <= ord('z')
        check3 = ord(c) >= ord('0') and ord(c) <= ord('9')
        return check1 or check2 or check3 