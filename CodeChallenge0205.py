# Frequent Words with Mismatches Problem

text = input('Enter text: ')
k = int(input('Enter k: '))
d = int(input('Enter d: '))


def Text(i, k):
    window = text[i:i + k]
    return window


def HammingDistance(p, q):
    length = len(p)
    z = 0
    for n in range(length):
        if p[n] != q[n]:
            z = z + 1
    return (z)


def ImmediateNeighbors(Pattern):
    # 1-neighborhood of Pattern (returns pattern with only one changed)
    Pattern_length = len(Pattern)
    Neighborhood = []
    for y in range(Pattern_length):
        symbol = Pattern[y]
        for x in "ACTG":
            if x != symbol:
                neighbor = Pattern[:y] + x + Pattern[y + 1:]
                Neighborhood.append(neighbor)
    return Neighborhood


def FirstSymbol(Pattern):
    # first base of pattern
    return (Pattern[0])


def Suffix(Pattern):
    # pattern starting from the second base
    return (Pattern[1:])


def Neighbors(Pattern, d):
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        one_base_list = ['A', 'G', 'C', 'T']
        return one_base_list
    Neighborhood = []
    SuffixNeighbors = Neighbors(Suffix(Pattern), d)
    for string_text in SuffixNeighbors:
        if HammingDistance(Suffix(Pattern), string_text) < d:
            for x in "ACTG":
                Neighborhood.append(x + string_text)
        else:
            Neighborhood.append(FirstSymbol(Pattern) + string_text)
    return Neighborhood


def MaxMap(freqMap):
    # returns maximum value from freqMap
    return max(freqMap.values())


def FrequentWordsWithMismatches(text, k, d):
    n = len(text)
    Patterns = ''
    #
    freqMap = {}
    # counts the number of times a given string has an approximate match in Text
    for i in range(0, n - k + 1):
        Pattern = Text(i, k)
        neighborhood = Neighbors(Pattern, d)
        for j in range(0, len(neighborhood)):
            neighbor = neighborhood[j]
            if neighbor not in freqMap.keys():
                freqMap[neighbor] = 1
            else:
                freqMap[neighbor] = freqMap[neighbor] + 1
    m = MaxMap(freqMap)
    for Pattern in freqMap:
        if freqMap[Pattern] == m:
            Patterns = Patterns + Pattern + ' '
    return Patterns

print(FrequentWordsWithMismatches(text, k, d))
