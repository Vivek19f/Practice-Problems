# Minimum AND xor OR

import sys
T = int(input())
for _ in range(T):
    n = int(input())
    li = list(map(int,input().strip().split()))[:n]
    li.sort()
    minXor=int(sys.float_info.max)
    val=0
    for i in range(0,n-1):
        val = ((li[i] ^ li[i+1]))
        minXor = min(minXor,val)
    print(minXor)