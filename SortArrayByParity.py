# https://leetcode.com/problems/sort-array-by-parity/

def sortArrayByParity(A):
        ret = [] * len(A)
        
        for i in range(len(A)):
            
            if A[i] % 2 == 0:                
                ret.insert(0, A[i])
            else:
                ret.append(A[i])
                
        return ret