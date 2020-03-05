input1 = input().split(" ")
values1 = list(map(int, input1))
N = values1[0]
K = values1[1]

input2 = input().split(" ")
layers = list(map(int, input2))
layers.sort()
layers = layers[::-1]

possible = [layers[0]]

for i in range(N):
    if (layers[i] + K )<= possible[-1]:
        possible.append(layers[i])
print(len(possible))