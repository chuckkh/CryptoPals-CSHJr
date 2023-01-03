inp1 = '1c0111001f010100061a024b53535009181c'
#... after hex decoding, and when XOR'd against:

inp2 = '686974207468652062756c6c277320657965'
#... should produce:

control = '746865206b696420646f6e277420706c6179'


def xor2(a, b):
    hxAlf = '0123456789abcdef'
    outp = ''
    for i in range(len(inp1)):
        outp += hxAlf[hxAlf.find(inp1[i]) ^ hxAlf.find(inp2[i])]
    return outp

res = xor2(inp1, inp2)
print(res, res == control)
