from math import *
pizzas = input("");
pizzaNums = pizzas.split();
pizzaTotals = [0,0,0]

for i in range(len(pizzaNums)):
    pizzaNums[i] = int(pizzaNums[i])

for i in range(len(pizzaNums)):
    pizzaTotals[i] = ceil(pizzaNums[i]/3)

total = sum(pizzaTotals)
print(total)