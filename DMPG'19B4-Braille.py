dict = {
    "a": [1, 0, 0],
    "b": [1, 1, 0],
    "c": [3, 0, 0],
    "d": [3, 2, 0],
    "e": [1, 2, 0],
    "f": [3, 1, 0],
    "g": [3, 3, 0],
    "h": [1, 3, 0],
    "i": [2, 1, 0],
    "j": [2, 3, 0],
    "k": [1, 0, 1],
    "l": [1, 1, 1],
    "m": [3, 0, 1],
    "n": [3, 2, 1],
    "o": [1, 2, 1],
    "p": [3, 1, 1],
    "q": [3, 3, 1],
    "r": [1, 3, 1],
    "s": [2, 1, 1],
    "t": [2, 3, 1],
    "u": [1, 0, 3],
    "v": [1, 1, 3],
    "w": [2, 3, 2],
    "x": [3, 0, 3],
    "y": [3, 2, 3],
    "z": [1, 2, 3],
    " ": [0, 0, 0],



}
config = {
    0: "..",
    1: "o.",
    2: ".o",
    3: "oo"
}

s1 = ""
s2 = ""
s3 = ""
str = input().lower()
word = list(str)
for i in range(len(word)):
    order = dict[word[i]]
    for n in range(3):
        if n == 0:
            s1+= config[order[n]]
        elif n == 1:
            s2+= config[order[n]]
        elif n == 2:
            s3+= config[order[n]]

print(s1)
print(s2)
print(s3)

"""
o.o.o..oo.o.o....o.o..o....oo.o.o...o.ooo..ooo
o.o...o.o.o..o..o.o.......oo.oo.o......o.ooo.o
..o.....o.o.......o........o..o.o...o.o.o..oo.

o.o.o..oo.o.o....o.o..o....oo.o.o...o.ooo..ooo
o.oo..o.o.o..o..o.o.......oo.oo.o......o.ooo.o
..o.....o.o.......o........o..o.o...o.o.o..oo.



"""