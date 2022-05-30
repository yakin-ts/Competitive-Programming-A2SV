#User function Template for python3

class Solution: 
    def select(self, arr, i):
        for n in range(len(arr)):
           i_current = arr[n]
           for y in range(n, len(arr),1):
               if(arr[y]<i):
                   i_current = arr[y]
        return i_current
    
    def selectionSort(self, arr,n):
        for m in range(len(arr)):
            current_min = arr[m]
            i_min = m
            for i in range(m,len(arr),1):
                if(arr[i]<current_min):
                    current_min = arr[i]
                    i_min = i
            temp = arr[m]
            arr[m] = current_min
            arr[i_min] = temp
                    
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends