def myfunc():
    input1 = input().split(" ")
    mylist = list(map(int, input1))

    if (mylist[0] > mylist[1] and mylist[0] > mylist[3]):
        if(mylist[2] > mylist[1] and mylist[2] > mylist[3]):
            return "trans"
    elif (mylist[1] > mylist[0] and mylist[1] > mylist[2]):
        if(mylist[3] > mylist[0] and mylist[3] > mylist[2]):
            return "trans"
    return "cis"

print(myfunc())