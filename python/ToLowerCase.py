class Solution:
    def toLowerCase(self, str):
        s = ''

        for c in str:
            if ord('A') <= ord(c) <= ord('A') + 25:
                s += chr(ord(c) - ord('A') + ord('a'))
            else:
                s += c
        
        return s