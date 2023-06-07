
W = 50

val = [60,100,120]
wt= [20,50,30]

ans = []
for i in range(len(val)):
    ans.append((val[i],wt[i]))
    
ans.sort(key=lambda x:x[0]/x[1],reverse=True)

tot = 0.0
for val,wt in ans:
    l = min(W,wt)
    tot += l*val/wt
    W-=l
print(tot)
