def fib(n):
    ans = 0
    for i in range(n-1):
        ans = arr[-1]+arr[-2]
        arr.append(ans)
arr = [0,1]

n = int(input())
fib(n)
print(arr[-1])
