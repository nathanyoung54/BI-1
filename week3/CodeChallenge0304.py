# Profile-most Probable k-mer Problem
text = input('Enter text: ')
k = int(input('Enter k: '))
profile = [
    [0.197, 0.333, 0.212, 0.273, 0.182, 0.227, 0.288, 0.197, 0.227, 0.273, 0.197, 0.227, 0.303, 0.182, 0.288],
    [0.242, 0.288, 0.273, 0.197, 0.348, 0.258, 0.197, 0.242, 0.333, 0.212, 0.303, 0.212, 0.318, 0.303, 0.182],
    [0.242, 0.258, 0.288, 0.167, 0.288, 0.227, 0.212, 0.303, 0.197, 0.152, 0.258, 0.303, 0.152, 0.303, 0.258],
    [0.318, 0.121, 0.227, 0.364, 0.182, 0.288, 0.303, 0.258, 0.242, 0.364, 0.242, 0.258, 0.227, 0.212, 0.273],

]
def Text(i, k):
    window = text[i:i + k]
    return window

def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    kmer_list = []
    pair_list = []
    probability_list = []
    for i in range(n-k+1):
        kmer = Text(i,k)
        kmer_list.append(kmer)
    for kmer in kmer_list:
        pair_list.append([kmer, ComputeProb(kmer, profile)])
        probability_list.append(ComputeProb(kmer, profile))
    max_prob = max(probability_list)
    for pair in pair_list:
        if pair[1] == max_prob:
            max_kmer = pair[0]
    return max_kmer



def ComputeProb(kmer, profile):
    prob = 1
    k = len(kmer)
    for i in range(k):
        if kmer[i] == 'A':
            prob = prob * profile[0][i]
        elif kmer[i] == 'C':
            prob = prob * profile[1][i]
        elif kmer[i] == 'G':
            prob = prob * profile[2][i]
        elif kmer[i] == 'T':
            prob = prob * profile[3][i]
    return prob






print(ProfileMostProbableKmer(text, k, profile))
