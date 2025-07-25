#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'subsetA' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def subsetA(arr):
    # Write your code here
    arreglo = list(arr)
    arreglo.sort(reverse=True)
    min = set(arreglo)
    return min
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for _ in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = subsetA(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()