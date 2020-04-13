class Solution:
    def reverseString(self, s):
        start = 0
        finish = len(s) - 1
        
        while start <= finish:
            temp = s[start]
            s[start] = s[finish]
            s[finish] = temp
            
            start += 1
            finish -= 1