# Median String Problem

Dna1 = ["CAGTTGAGAGCTTACGTAACTGGCGACCGAAAAGTGCGACAG"
"ATAATTAGTGTGTGGTATATGATACCGTGTGTTGCTTAAGTA",
"AGTCACATCCCTTAGGTAGACGTACAACATGATCCCCGTGCA",
"TTCTGCTCGGATTCATAAACGGTCAGGCGATAAGTACGGATA",
"CCAGTCAACCTGCATCGGCTGAGTTGTGGGGAGAGTTAAGTA",
"AGAGTGGTATCTTACGTAAACTGGCTGCCGGCAGGTTAGCCT",
"CGCTGTTTCCCATCATATCAGGCCCGACCTGATACGTAAGTA",
"GTTGGATGTTAGGATTGGTAACACTATGTAGTCCCCTATGCG",
"TGCGGGTGACACCCTAGTCGATCGGGCCTATTAGGGTATGTA",
"GCAGGTGGAGGCGTATCGTAGGTACGTGCCCCCTTCGTAACC"]
  
k = int(input('Enter k: '))

def HammingDistance(p, q):
    length = len(p)
    z = 0
    for n in range(length):
        if p[n] != q[n]:
            z = z + 1
    return (z)

def min_ham(pattern, text):
    # returns the kmer in text that has minimum ham_dis with Pattern
    index = 0
    n = len(text)
    k = len(pattern)
    min_ham = k
    for i in range(n-k+1):
        curr_ham = HammingDistance(text[i:i+k], pattern)
        if curr_ham < min_ham:
            min_ham = curr_ham
            index = i
    return text[index:index+k]

def d_text(pattern, text):
    # returns minimum distance
    pattern_prime = min_ham(pattern, text)
    d_text = HammingDistance(pattern, pattern_prime)
    return d_text

def d_motif(pattern, Dna):
    # returns the sum of all minimum distances
    # DistanceBetweenPatternAndString
    d_text_list = []
    for text in Dna:
        ling = d_text(pattern, text)
        d_text_list.append(ling)
    SUM = sum(d_text_list)
    return SUM

def KmerGenerator(k):
    nucleotides = "AGCT"
    kmer_list = ["A", "C", "G", "T"]
    new_list = []
    while len(kmer_list[0]) < k:
        for nucleotide in nucleotides:
            for item in kmer_list:
                new_list.append(nucleotide+item)
        kmer_list = new_list
        new_list = []
    return kmer_list


def MedianString(Dna, k):
    import math
    kmer_list = KmerGenerator(k)
    distance = math.inf
    for pattern in kmer_list:
        if distance > d_motif(pattern, Dna):
            distance = d_motif(pattern, Dna)
            Median = pattern
    return Median



#print(min_ham(pattern, text))
#print(d_text(pattern, text))
#print(d_motif(pattern, Dna))
print(MedianString(Dna, k))
