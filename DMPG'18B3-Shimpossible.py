n = int(input())
lengths = []
words = []
love = []

for i in range(n):
    temp = input().split(" ")
    lengths.append(int(temp[0]))
    words.append(temp[1])

for i in range(len(lengths)):
    found = False
    c = 2
    length = lengths[i]
    word = words[i]
    
    while not found:

        start = 0
        end = 0
        subs = []
        same = 0
        if length % c == 0:
            d = int(length / c)
            for i in range(c):
                end += d
                subs.append(word[start:end])
                start += d
            for i in range(len(subs)):
                first = subs[0]
                if subs[i] == first:
                    same += 1
                if same == len(subs):
                    wordlen = len(subs[0])
                    subslen = len(subs)
                    love.append(wordlen/subslen)
                    found = True

        c += 1
        
love.sort()
print(love[-1])