from math import inf

s1 = "this is a test"
s2 = "wokka wokka!!!"

def hamming(a, b):
    lena = len(a)
    if lena != len(b):
        return -1
    total = 0
    for ind in range(lena):
        b1 = bin(ord(a[ind]) + 2**16)[-8:]
        b2 = bin(ord(b[ind]) + 2**16)[-8:]
        lenb1 = len(b1)
        for cind in range(lenb1):
            total += b1[cind] != b2[cind]
    return total

def hammingInt(a, b):
    total = 0
    lena = len(a)
    if lena != len(b):
        return -1
    for ind in range(lena):
        aa = a[ind]
        bb = b[ind]
        while aa or bb:
            total += abs((aa%2) - (bb%2))
            aa//=2
            bb//=2
    return total

#print(hamming(s1, s2))

b64alf = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

f = open("6.txt", "r")
text = []
#lines = f.readlines()
for line in f.readlines():
    line = line.replace("=", "A")
    hexLine = []
    ll = len(line) - 1
    for cind in range(0, ll, 4):
        c1 = line[cind]
        c2 = line[cind+1]
        c3 = line[cind+2]
        c4 = line[cind+3]
        b1 = (b64alf.index(c1) << 2) + (b64alf.index(c2) >> 4) & 0xff
        b2 = (b64alf.index(c2) << 4) + (b64alf.index(c3) >> 2) & 0xff
        b3 = (b64alf.index(c3) <<6) + (b64alf.index(c4)) & 0xff
        hexLine.append(b1)
        hexLine.append(b2)
        hexLine.append(b3)
    text.extend(hexLine)


bestKeyLengths = [(inf, 0), (inf, 0), (inf, 0)]
for keyLength in range(2, 50):
    kl2 = keyLength*2
    kl3 = keyLength*3
    kl4 = keyLength*4
    w1 = text[:keyLength]
    w2 = text[keyLength:kl2]
    w3 = text[kl2:kl3]
    w4 = text[kl3:kl4]
    d1 = hammingInt(w1, w2) / keyLength
    d2 = hammingInt(w2, w3) / keyLength
    d3 = hammingInt(w3, w4) / keyLength
    d = (d1 + d2 + d3) / 3
#    d = (d1 + d3) / 2
    mkl = max(bestKeyLengths)
    if d < mkl[0]:
        bestKeyLengths.remove(mkl)
        bestKeyLengths.append((d, keyLength))
bestKeyLengths.sort()
#print(bestKeyLengths)

keys = []
for tup in bestKeyLengths:
    theKey = []
    keyLength = tup[1]
    shiftedBlocks = []
    tl = len(text)
    tk = tl // keyLength
    for i in range(keyLength):
        block = []
        for offset in range(tk):
            block.append(text[offset * keyLength + i])
        shiftedBlocks.append(block)
    for block in shiftedBlocks:
        minNonsense = inf
        bestKey = 0
        for key in range(1,255):
            nonsense = len(block)*2
            for c in range(97,122):
                nonsense -= block.count(key ^ c)
            for c in [97, 101, 110,115,116 ]:
                nonsense -= block.count(key ^ c)
            if nonsense < minNonsense:
                minNonsense = nonsense
                bestKey = key
        theKey.append(chr(bestKey))
    keys.append(theKey)
#    print(keyLength, theKey)

bestFinalScore = 0
bestFinalKey = 0
decs = []
for kind in range(len(keys)):
    key = keys[kind]
    kl = len(key)
#    print(kl)
    dec = ''
    tl = len(text)
    finalScore = 0
    for cind in range(tl):
        asc = text[cind] ^ ord(key[cind%kl])
        c = chr(asc)
        if 96 < asc < 123:
            finalScore += 1
        dec += chr(text[cind] ^ ord(key[cind%kl]))
    decs.append(dec)
    if finalScore > bestFinalScore:
        bestFinalScore = finalScore
        bestFinalKey = kind
#    print(dec)
#for k in keys[-1]:
#    print(k, end='')
print("Key:")
for c in keys[bestFinalKey]:
    print(c, end='')
print()
print()
print("Decoded text:")
print(decs[bestFinalKey])
