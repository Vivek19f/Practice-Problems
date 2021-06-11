# Monk and Inversions

# Input:
# First line consists of a single integer T denoting the number of test cases.
# First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers denoting the matrix M.

# Output:
# Print the answer to each test case in a new line.


# Write your code here
T = int(input())
for _ in range(T):
    n = int(input())
    mat=[]
    for i in range(n): 
        mat.append([int(j) for j in input().split()])
    c = 0
    for i in range(n):
        for j in range(n):
            for p in range(i,n):
                for q in range(j,n):
                    if i<=p and j<=q:
                        if mat[i][j]>mat[p][q]:
                            c+=1
    print(c)