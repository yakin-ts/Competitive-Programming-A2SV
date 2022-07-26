class Solution:
    def findKthBit(self, n: int, k: int) -> str:
    # Recursion subroutine
        def recurse(n):
            if n==1:
                return '0'
            else:
                ans = recurse(n-1)
                ans = ans + '1' + invert(ans)
            return ans
        
    # String Invert subroutine
        def invert(string):
            res = ['0' if i=='1' else '1' for i in string]
            return "".join(res)[::-1]
        
        return recurse(n)[k-1]