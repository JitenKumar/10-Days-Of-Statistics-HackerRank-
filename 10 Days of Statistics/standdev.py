n = int(input())
num = list(map(int,input().split()))
def mean(num):
    return (sum(num)/len(num))
s = 0
m = mean(num)

for i in range(n):
    s += (num[i]-m)**2

print(round((s/n)**.5,1))