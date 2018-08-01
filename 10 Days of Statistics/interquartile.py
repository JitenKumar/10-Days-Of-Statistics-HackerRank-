import statistics as st
n = int(input())
num = list(map(int,input().split()))
freq = list(map(int,input().split()))
temp = []
for i in range(n):
    temp += [num[i]] * freq[i]
N = sum(freq)
temp.sort()
if N % 2 is not 0:
    q1 = st.median(temp[:N//2])
    q3 = st.median(temp[N//2+1:])
else:
    q1 = st.median(temp[:N//2])
    q3 = st.median(temp[N//2:])
print(round(float(q3-q1),1))
