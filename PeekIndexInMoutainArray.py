# https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, A):
        for i in range(len(A)):
            if A[i] > A[i+1]:
                return i