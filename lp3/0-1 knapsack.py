val = [1,2,5,6]
wt = [2,3,4,5]
W = 8
n = len(val)
arr = [[0 for x in range(W+1)] for x in range(n+1)]
for i in range(n+1):
    for j in range(W+1):
        if wt[i-1]>j:
            arr[i][j] = arr[i-1][j]
        else:
            arr[i][j] = max(arr[i-1][j],(arr[i-1][j-wt[i-1]])+val[i-1])
            
print(arr[n][W])
