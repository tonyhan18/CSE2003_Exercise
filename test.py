import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n = int(input())
a = list(list(map(int,input().split())) for _ in range(n))
d=[-1] * (n+1)
d[0] = 0

for i in range(n):
    if(a[i][0]+i <= n):
        if(d[i+a[i][0]] == -1 or d[i]+a[i][1] > d[i+a[i][0]]):
            d[i+a[i][0]] = d[i] + a[i][1]
    d[i+1] = max(d[i],d[i+1])

print(d[n])
