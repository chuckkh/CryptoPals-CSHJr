import time
from math import inf

f = open("4.txt", "r")
useful = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,"

lineNumber = 0
line = 0
bestKey = 0
decoded = ''
minNonsense = inf

start = time.time()

lineIndex = 0

for enc in f.readlines():
    letters = [enc[i:i+2] for i in range(0, len(enc) - 1, 2)]
    for key in range(0,256):
        nonsense = 30
        for c in useful:
            cenc = str(hex(ord(c) ^ key))[2:]
            nonsense -= letters.count(cenc)
        if nonsense < minNonsense:
            line = enc
            minNonsense = nonsense
            bestKey = key
            lineNumber = lineIndex
    lineIndex += 1
    
letters = [line[i:i+2] for i in range(0, len(line) - 1, 2)]
for letter in letters:
    decoded += chr(int(letter, 16) ^ bestKey)

lap1 = time.time()
print("Time:", lap1 - start)
print("Line number:", lineNumber)
print("Key:", bestKey)
print("Encoded:", line)
print("Message:", decoded)
