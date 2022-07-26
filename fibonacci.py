class Solution:
    def fib(self, n: int) -> int:
        fbmem = {i+1:-1 for i in range(n)}
        def helper(n,mem):
            if n==0:
                return 0
            elif n==1 or n==2:
                return 1
            else:
                if mem[n]==-1:
                    mem[n] = helper(n-1,mem) + helper(n-2,mem)
            return mem[n]
        return helper(n,fbmem)
    