# Implanted Motif Problem: Find all (k, d)-motifs in a collection of strings.

Dna = ['ACACAATAGAAGCCCAACACGCTGG','TTTTGAATCCAACCGTAGGTCCCGA','GTATTAATCCGGGTGTTTTGATGAC','CATCAGTACGAAACCAACACGAGCG','CCGTAGGGTCTCCATAACGCTGCAT','TACGTGAGAAAAACCTGCATCAAGT']
k = int(input('Enter k: '))
d = int(input('Enter d: '))


def Text(text, i, k):
    window = text[i:i + k]
    return window


def HammingDistance(p, q):
    length = len(p)
    z = 0
    for n in range(length):
        if p[n] != q[n]:
            z = z + 1
    return (z)


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


def MotifEnumeration(Dna, k, d):
    patterns = set()
    n = len(Dna)
    AllKmers = []
    for j in range(n):
        text = Dna[j]
        kmers = []
        n_1 = len(text)
        for i in range(n_1 - k +1):
            kmers.append(text[i:i+k])
            # append all k-mer window to kmers list
        neigh = []
        for i in range(len(kmers)):
            L = Neighbors(kmers[i], d)
            # list of all d-neighbours for one k-mer in kmers list
            for val in L:
                neigh.append(val)
        AllKmers.append(neigh)
    x1 = set(AllKmers[0])
    x2 = set(AllKmers[1])
    patterns = x1 & x2
    for y in range(2, len(AllKmers)):
        patterns = patterns & set(AllKmers[y])
    patterns = list(patterns)
    string = ""
    for i in patterns:
        string = string + i + " "
    return string

print(MotifEnumeration(Dna, k, d))



