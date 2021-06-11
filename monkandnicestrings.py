# Monk and Nice Strings

arr = []
n = int(input())
for i in range(n):
    arr.append(input())
    count = 0
    for j in range(0,i):
        if arr[i] > arr[j] :
            count +=1
    print(count)