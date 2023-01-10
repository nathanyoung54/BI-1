#Frequent Words Problem
text = input('Enter Text: ')
k = int(input('Enter k: '))

def Text(i, k):
    mer = text[i:i+k]
    return mer

def FreqeuncyTable(text, k):
    freqMap = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = Text(i, k)
        if pattern not in freqMap:
            freqMap[pattern] = 1
        else:
            freqMap[pattern] = freqMap[pattern] + 1
    return(freqMap)


def MaxMap(freqMap):
    return max(freqMap.values())

def BetterFrequentWords(text, k):
    FrequentPatterns = []
    freqMap = FreqeuncyTable(text, k)
    for Pattern in freqMap.keys():
        if freqMap[Pattern] == MaxMap(freqMap):
            FrequentPatterns.append(Pattern)
    print(FrequentPatterns)

BetterFrequentWords(text, k)


