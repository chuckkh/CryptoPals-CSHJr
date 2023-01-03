from math import ceil
dec = ["Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"]

key = "ICE"
keyLen = len(key)
keyIndex = 0


enc = []
for line in dec:
    encLine = ''
    for c in line:
        decC = ord(c)
        keyC = ord(key[keyIndex])
        keyIndex = (keyIndex + 1) % keyLen
        encC = decC ^ keyC
        encLine += str(hex(encC))[2:]
    enc.append(encLine)

for line in enc:
    lineLen = ceil(len(line) / 74)
    for i in range(lineLen):
        start = i*74
        print(line[start : start + 74])




















