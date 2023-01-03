hx = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def hexToBase64(hxInp):
    hAlf = '0123456789abcdef'
    bSix = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    hxOutp = ''
    bit6 = 0
    mod3 = 0
    for hxChar in hxInp:
        if mod3%3 == 0:
            bit6 = hAlf.find(hxChar) << 2
        elif mod3%3 == 1:
            nextB = hAlf.find(hxChar)
            bit6 += nextB >> 2
            hxOutp += bSix[bit6]
            bit6 = (nextB & 0b11) << 4
        elif mod3%3 == 2:
            bit6 += hAlf.find(hxChar)
            hxOutp += bSix[bit6]
        mod3 = (mod3 + 1) % 3
    return hxOutp

print(hexToBase64(hx))

        
