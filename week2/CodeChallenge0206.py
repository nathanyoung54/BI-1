# Frequent Words with Mismatches and Reverse Complements Problem

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

def Count(text, pattern, d):
    t = len(text)
    k = len(pattern)
    z = 0
    for i in range(0, t - k + 1):
        window = text[i:i + k]
        if HammingDistance(window, pattern) <= d:
            z = z + 1
    return z

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

def RevComp(text):
    list = []
    for base in text:
        if base == 'A':
            list.append('T')
        elif base == 'G':
            list.append('C')
        elif base == 'C':
            list.append('G')
        elif base == 'T':
            list.append('A')
    ReverseList = list[::-1]
    patternRC = ''
    for b in ReverseList:
        patternRC = patternRC + b
    return patternRC

def FrequentWordsWithMismatchesandRC(text, k, d):
    n = len(text)
    Patterns = ''
    freqMap = {}
    rev_text = RevComp(text)
    #freqMapRC = {}
    #freqMapComb = {}
    # counts the number of times a given string has an approximate match in Text
    for i in range(0, 4**k):
        freqMap[i] = 0
    for i in freqMap:
        count = 0
        rc_count = 0
        count = Count(text, NumberToPattern(i, k), d )
        rc_count = Count(rev_text, NumberToPattern(i, k), d)
        freqMap[i] = count + rc_count
    return freqMap

def PatternToNumber(pattern):
    if len(pattern)==0: return
    SymbolToNumber = {'A':0,'C':1,'G':2,'T':3}
    if len(pattern)==1: return SymbolToNumber[pattern]
    n=len(pattern)
    symbol=pattern[n-1]
    prefix=pattern[:n-1]
    return (4*PatternToNumber(prefix)+SymbolToNumber[symbol])

def NumberToPattern(index,k):
    NumberToSymbol = {0:'A',1:'C',2:'G',3:'T'}
    if k==1: return NumberToSymbol[index]
    prefix_index=index//4
    r=index%4
    symbol=NumberToSymbol[r]
    return NumberToPattern(prefix_index,k-1)+symbol


approx_kmers = FrequentWordsWithMismatchesandRC(text, k, d)
for a in approx_kmers:
    if approx_kmers[a] == max(approx_kmers.values()):
        print(NumberToPattern(a, k), end=' ')

