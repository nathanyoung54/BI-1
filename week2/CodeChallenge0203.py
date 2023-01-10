# Approximate Pattern Matching Problem

text = input('Enter text: ')
pattern = input('Enter pattern: ')
d = int(input('Enter d: '))

def HammingDistance(p, q):
    length = len(p)
    z = 0
    for n in range(length):
        if p[n] != q[n]:
            z = z + 1
    return(z)

def AppMatch(text, pattern, d):
    t = len(text)
    k = len(pattern)
    z = ''
    for i in range(0, t-k+1):
        window = text[i:i+k]
        if HammingDistance(window, pattern) <= d:
            z = z + str(i) + ' '
    print(z)

def Count(text, pattern, d):
    t = len(text)
    k = len(pattern)
    z = 0
    for i in range(0, t - k + 1):
        window = text[i:i + k]
        if HammingDistance(window, pattern) <= d:
            z = z + 1
    print(z)

Count(text, pattern, d)