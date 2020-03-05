nums = input().split(" ")
nums1 = list(map(int, nums))

N = nums1[0]
M = nums1[1]
counter = 0
plant = []
printPlant = []
for i in range(M):
    temp1 = list(input())
    plant.append(temp1)
print()
for i in range(M):
    tempstr = ""
    for n in range(len(plant[i])):
        if plant[i][n] == " ":
            tempstr += " "
        if plant[i][n] == "#":
            tempstr += "#"
        if plant[i][n] == "o":
            tempstr += " "
            counter += 1
        if plant[i][n] == "*":
            tempstr += " "
    printPlant.append(tempstr)
for i in range(M):
    print(printPlant[i])
print(counter * "o")