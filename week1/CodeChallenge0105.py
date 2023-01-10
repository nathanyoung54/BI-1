text = input('Enter Text: ')
k = int(input('Enter k: '))
L = int(input('Enter L: '))
t = int(input('Enter t: '))

def Text(i, k):
    mer = text[i:i+k]
    return mer

def FreqeuncyTable(text, k):
    freqMap = {}
    n = len(text)
    for i in range(n-k+1):
        window = Text(i, k)
        if window not in freqMap:
            freqMap[window] = 1
        else:
            freqMap[window] = freqMap[window] + 1
    return(freqMap)

def FindClumps(text, k, L, t):
    patterns = ''
    freqMap = FreqeuncyTable(text, k)
    for s in freqMap.keys():
        if freqMap[s] >= t:
            patterns = patterns + s + ' '
    print(patterns)

FindClumps(text, k, L, t)