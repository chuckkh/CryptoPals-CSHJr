import time

enc = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'


maxVowels1 = 0
maxVowels2 = 0
bestKey1 = 0
bestKey2 = 0
decoded1 = ''
decoded2 = ''
letters = [enc[i:i+2] for i in range(0, len(enc), 2)]

start = time.time()

for key in range(0,256):
    encVowels = []
    totalLowercaseVowels = 0
    for v in 'aeiou':
        c = str(hex(ord(v) ^ key))[2:]
        encVowels.append(str(hex(ord(v) ^ key))[2:])
        totalLowercaseVowels += letters.count(c)
    if totalLowercaseVowels > maxVowels1:
        maxVowels1 = totalLowercaseVowels
        bestKey1 = key
for letter in letters:
    decoded1 += chr(int(letter, 16) ^ bestKey1)

lap1 = time.time()

for key in range(0,256):
    vowels = 0
    dec = ''
    for letter in letters:
        c = chr(int(letter, 16) ^ key)
        if c in 'aeiou':
            vowels += 1
        dec += c
    if vowels > maxVowels2:
        maxVowels2 = vowels
        bestKey2 = key
        decoded2 = dec

lap2 = time.time()

print("Counting encoded lowercase vowels for each key before decoding the string:")
print(bestKey1, decoded1)
print("Time:", lap1 - start)
print()
print("Decoding the string for each key and then counting lowercase vowels:")
print(bestKey2, decoded2)
print("Time:", lap2 - lap1)
