N = int(input())
nums = []
neg = []
mult = []
total = 1
for i in range(N):
    temp1 = int(input())
    nums.append(temp1)
nums.sort()

for i in range(N):
    if nums[i] > 0:
        mult.append(nums[i])
    if nums[i] < 0:
        neg.append(nums[i])
neg.sort()
if len(neg) % 2 == 0:
    for i in range(len(neg)):
        mult.append(neg[i])
elif len(neg) % 2 == 1:
    for i in range(len(neg) - 1):
        mult.append(neg[i])

for num in mult:
    total *= num

if total == 1:
    total = nums[-1]
print(total)