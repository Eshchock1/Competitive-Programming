numsInput = input().split(" ")
nums = list(map(int, numsInput))

A = nums[0]
B = nums[1]
max = 0

if A >= B - 1:
    print(B-1)

else:
    print(A)