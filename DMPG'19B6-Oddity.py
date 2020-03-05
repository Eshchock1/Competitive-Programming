buy = 0
def myfunc():

    input1 = input().split(" ")
    N = int(input1[0])
    K = int(input1[1])
    input2 = input().split(" ")
    costs = list(map(int, input2))
    allPeopleOdd = False
    elim1 = []
    elim2 = []
    collections = []

    for i in range(N):
        temp1 = input().split(" ")
        values = list(map(int, temp1))
        collections.append(values)


    for i in range(N):
        counter = 0
        for n in range(K):
            if collections[i][n] == 1:
                counter += 1
        elim1.append(counter)

    for number in elim1:
        elim2.append(number % 2)
    setelim = set(elim2)
    elim2 = list(setelim)
    if len(elim2) != 1:
        return -1
    if elim1[0] % 2 == 1:
        allPeopleOdd = True


    costs.sort()
    if allPeopleOdd == True:
        buy = costs[1] + costs[0]
        return buy

    else:
        buy = costs[0]
        return buy



print(myfunc())