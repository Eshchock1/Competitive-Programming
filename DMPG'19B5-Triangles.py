def myfunc():
    num = int(input())
    points = []
    pointsUnsorted = []
    for i in range(num):
        temp1 = input().split(" ")
        temp2 = list(map(int, temp1))
        points.append(temp2)
        pointsUnsorted.append(temp2)

    points.sort()

    for i in range(len(points) - 2):
        c1 = points[i][2]
        c2 = points[i + 1][2]
        c3 = points[i + 2][2]
        if c1 != c2 or c1 != c3 or c2 != c3:
            point1 = pointsUnsorted.index(points[i])
            point2 = pointsUnsorted.index(points[i + 1])
            point3 = pointsUnsorted.index(points[i+2])
            return str(point1 + 1) + " " + str(point2 + 1) + " " + str(point3 + 1)
    return -1
print(myfunc())