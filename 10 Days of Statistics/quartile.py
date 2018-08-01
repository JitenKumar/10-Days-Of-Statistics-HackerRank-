n = int(input())
numbers = sorted(list(map(int,input().split())))
def median(num):
    if len(num)%2==0:
        return int(sum(num[len(num)//2-1:len(num)//2+1]) / 2)
    else:
        return int(len(num//2))
def quart(n,nums):
    q1 = median(nums[:len(nums)//2])
    q2 = median(nums)
    if n%2==0:
        q3 = median(nums[len(nums)//2:])
    else:
        q3 = median(nums[len(nums)//2:])
    return q1,q2,q3
q1,q2,q3 = quart(n,numbers)
print(q1)
print(q2)
print(q3)
