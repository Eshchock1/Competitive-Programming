def count():
    input1 = input()
    text = list(input1)
    num = int(input())
    counter = 0
    for i in range(len(text)):


        if text[i] == "S":
            counter += 1
        elif text[i] == "R":
            counter = 0
        if counter >= num:
            return "Spamming"
    return "All good"

print(count())