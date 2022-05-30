#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    last = arr[len(arr)-1]
    notComplete = True
    for idx in range(len(arr)-1,-1,-1):
        for idx2 in range(idx-1,-1,-1):
            marked = idx2 + 1
            if ((arr[marked] <= arr[idx2]) and notComplete):
                # last = arr[marked]
                arr[marked] = arr[idx2]
                print(*arr)
            else:
                if((arr[idx2]> last) and notComplete):
                    arr[marked] = arr[idx2]
                    print(*arr)
                    if(idx2==0):
                        arr[idx2] = last
                        notComplete =False
                        print(*arr)
                elif  ((arr[idx2]<last) and notComplete):
                    arr[marked] = last
                    notComplete = False
                    print(*arr)
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
