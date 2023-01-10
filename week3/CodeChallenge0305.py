# GreedyMotifSearch Problem

from collections import Counter

import numpy as np

k = int(input('Enter k: '))
t = int(input('Enter t: '))
Dna = ["GTACGACATTTCAGGCCTATGACTATGACACGAAAATTTGAGTGTGCAGAACTCTGAGTGTCGGCCGTTATCTTGGACTATGAGCAAACCTTGCATGGGAGGCGCCAAAGCGTAGTAAGTACGATTCGTGTGCAGGAGGGGACGCCTGATAGAACT",
"GGTACGGTATTCGTAAAGTTCTGTAACCTCGCGCAACGTTAACAGTTTGAATGGACAGGGAGGCCGCTCCCTAGTTTCTTGCGGTACGACAAAACCAGGCTAGGTACTATACCAGAAGGTACCCACCCGGCGGATCCAATCTCCTATCGTGTCGCG",
"TGTCGGAGGGCCCAAGTTGATCGATTCACTCAGCACGGCACGAGAAGGAGAATCGCCCCGTGCGGTACAGACATCTAAACGAGGAGGCCCCTAACTGCTTACTTAATTAAAGCTCCCATGCTACATGGCCGTACTTTCCGAATCCGCAACCGCGGG",
"GTTTTAAGGCACCAAGATCTGGACAGGCCACTATCTACCGTAACGCTACATTACCTACCGAACTCTTTGCACTCAAAATTATTGAGTAAGCTGCTGATAATCTAGGTTATGAAGCTAAGTTCATATGGCCCTCTCTAACTCAGAAAGGCTCTGCGT",
"GCGTTTACGTGTCAGAACTCATATGGCAGCCAACTCAGGCCGATTACTCCGTTCACCGAGTATGAGCACTAAGCGAATTATTCAGATCGTTTATGATGAGTCCACAACTATGGCAATTCATATCGTAGCCGCGAGCAATCTTTAGCAGGCCAGCAC",
"TTTATGTGAGTCCAAATCCCTGGAGTGATTCAGGCCTCTTATTGCTCCGGTTTAGATTATTGGAGGGTCGTGAGGAATGACTTGTTAGTCGAACTCAGGCCGGTGTCTTCAACGTTGCGTTGGCGAGATTATGATCGCTTGTATACCCCACCCGAT",
"TTCACCGCTTTCAGGGACGAAGCTAAGGACCACGTGAAGTAGGCCCGCAGGCCTTTCTCTTCCTCCGAAGGTTATCGCTGGAAGGTTCTCCACCAGGACGTTGACTATAATCAGCAGCGTGGGCCGGAAGATTGGGGAGATCCATCCATTCACGCA",
"GCGATCGGACCCTTGTCAACATGAACAGAGAGCCCACTCATGGTTTTCTCTGAACATGAGGCATCAGTAGCGAGGCCATTGCCTTGAAGGTGGGGCTAAGCCTGTAGAACTGCAGGATCACTGCACTGATATCGGGCTGCCGGGCATCTGAGAGAT",
"TGATTTTATGCTGACGTAGCAAAGTAATTTATAGGAGTAATTACATATCGAATACTTCTTGCTAATGTGATTAGACCCATTACCTGATAGAGAAAGCTCCAATAAACACTTCATGTGCTTTACGTGTCAATCCATTCGTAATTCAGGCCACTCTCT",
"GTCCCCGCTGTGACTTATAGAACTATTCAGTGTTAAACACAGTGTCCAGCCTAATCACTGAGGCCGTTCGCTAGCCCTTGGGACTACTTAGCTCTGTCCCCCGTTCTTGAAAGGCCTCTAGAACGCATGTAAGCCGCGGAAATCAGTTAAAGCTTT",
"TAAACTGCGGGGAGGCCGACTTGCTTGCGCATGCAAGTACCCTTAACTGTCAACTTACTGCTCGGCCGGGGGATCTCTTTCCGAAAAGTCTAGTCGTGACCACTCAACCTAACCAGGGAAAGGCCCATAACTAAGGAACCCTGTACTTTATACTAA",
"CACCCGATTATGAGGCCCGTTGCTCAGAGAGTGGTGCACCGTTTAGGGCTTTCTGAGTTCATGCCCACCCTGTGGCGGATAACCTTGCCCCCGTCTTGCCTATTGTGTCCGAAAGGCTGACTTTGGGGTTGCTCATCCAGTACCGGCTTATGGAAT",
"TGCGAGTACCGAAATATGCATAAACGGAATTATAAGAAGTATAGATGAGAGGAAGCCGGGAGGCCTTTATCTTTAGTAGGTACTGGCTACCGATAACTGGTGCATGCAGCCCAACTCTGTGATACCAAAATTACGTCCCATAGATCGGTTGATCAG",
"GTCTTCTGCTGTCTGGTCCAGTCATGTAGGCCAGCAGTGTGGATGAGGGAAAGAGGTGATCGGTACTTCACGGATCTCACAGCCCATCCGCCCTGGAGGCCCGTGCCTTGTAGTCTCCGGCTGTTACGATCTCTAACTCCCCCGTATCGCATTGGC",
"ATCTCGGGCTCCGCTCCAGGTGCGTAATAGGAGAAAGGACGGTTCCATAGGCCACTGCCTGCGACTGTTCACAACGTCTTCGGGTCACAGCGCTCACTGCTCCAATACGTGCTTCCAGGTTCACTCCTCCTGTCTCGAGGAGACAGAAGGCACCTT",
"CAGGGTCTGTCCCGCGGGTTCGAACGTACCGTTTTAAACGACTCTAGAGCGGGCCCATGTACGCAATGATACGGATGCCATCGTCTTTACTGGGCATAGTCTTAACCCAGGCCAATATCTGTACTCATGAACCGCTGGAGTTATCCTCTAATTAGT",
"CGGTGCCGGGGGGGACCCGTCTCATAATCTGATCTGCCCATGCTAGGTAATAGCTTGGGCAAAAATAGTGACTCCACCCGTACGAGGCCTTTCTCTCTCTCGCTTACGCGTCGGGTAGTTACATCGGCCTTTAACCGGGAGTAGATCCTAGCAGGA",
"AGGCCGTTGCCTGTACGAGAACCTTGCCGTGAGGGTGTAATCTCAGTTATTTCTAACTCGTAGAAGGCAAACGAGCACTATGTCGGTATAAAAACTTCGATGCTGGTATATTAATGTCTAGACTCTGTATGTGCTGTAATAATTGACATCAGCCTT",
"GAAATGAAGGATGGGTTAATAGCAAATCTAACCGGAGCAACTGGCTGAAATGGCTGAGTTGCGCCGGGAAAGTACACTGCGCGAAGGCCGGTGGCTCTGGCCTAATCTTTTGTGCATAACGGTGTGCTGTGGTCGCGTATCCAAATTCCTTGGCTA",
"ACAGTTCTCTCGGGTACAAGAGCTAAGGGACCGAGGAGGCCCGTCGCTTGCTTACAGCGAATCATAACTCACTTGCTGTTGCTACTCTGTATGGTAAAGCCCCCGGGGGAAGTAGTATGGTGCCTGGCTTTGACCCTACTTGCGCTAACTTTTAAG",
"TTAAACGGATATAGGAAGCACCTAAGGCCTGTCCCTAGATGATGATTAGGAAAGTTGAATGTCGTTTTCAGGGCTTTTAAAGTTAATAACCGCGGGTCGTAGTCACTGTTAATCGACGTCGGCGTATGAAATACACTTGGCATAGAATAGTGCCTC",
"AGAGTTAAATGCTGGGATTTTAGGAGTACCAGTAGGCCCAAACCCTTTACTTTGTAGGGTTGAAGAATAGAGCGTAGCGGTACAACGTACGCTCTCTAGCGATGTGTAACTGCTACCGGAAACGGAAATCAAAGGCCTATTGCTAACGTTCTTCGC",
"TGGCCTGTAGCCTTGCTCAAGCAACGCTACGGAGTACTGATTGACCAAGCTCTCCAGGTGGCTGGATGCTGGAGGCCTTTGCCTACTCATCATTCTCCAAGGCTGCGCAGCGGGCAGTCTAATTCAATTCGAAGGCTCACGTCGGCACTTCCCGCC",
"TATGAGTAATCTGCACTGGGCAGGAGGCCCTTCCCTGTTTTAATGCTCAAATAACTCCGGAGCTCCTTTAACCTCCGCGCTTAGTTGTAACGAACCTTCGGTGCAGTTGTTCGATGGTGGAAGACCTCCCGTCTACGAGTAGGAAGTTTCTACGAA",
"GTGCGGCCACAGTTTTCTCCCAGCACGTAACCAGGATGGCATAGGGAAAGGTTCACATCCTTCAATCAAGATATCGCGGGTGTCGTTTGCCTTACTGTGCACAGGAAATATCAGAGGTGCAGCAAGTGCCGTAGGCCAGTCTCTTCTTTGTCCGAC"]
#Dna = ["GCCAA", "GGCCTG", "AACCTA", "TTCCTT"]

def Score(Motifs):

    Motifs_arr = np.array([list(seq) for seq in Motifs])
    count_matrix = np.zeros((4, Motifs_arr.shape[1]))

    score_list = []
    for i in range(Motifs_arr.shape[1]):
        column_i = Motifs_arr[:, i]
        # columns
        len_column_i = column_i.shape[0]
        # length of column = 10
        count = Counter(column_i)
        A_count = count["A"]
        C_count = count["C"]
        G_count  = count["G"]
        T_count = count["T"]
        max_count = max(A_count, C_count, G_count, T_count)
        score = len_column_i - max_count
        score_list.append(score)
        Sum = sum(score_list)

    return Sum

def Profile(Motifs):
    Motifs_arr = np.array([list(seq) for seq in Motifs])
    profile_matrix = np.zeros((4, Motifs_arr.shape[1]))

    for i in range(Motifs_arr.shape[1]):
        column_i = Motifs_arr[:, i]
        # columns
        len_column_i = column_i.shape[0]
        # length of column = 10
        count = Counter(column_i)
        profile_matrix[0, i] = count["A"] / len_column_i
        profile_matrix[1, i] = count["C"] / len_column_i
        profile_matrix[2, i] = count["G"] / len_column_i
        profile_matrix[3, i] = count["T"] / len_column_i

    profile_list = profile_matrix.tolist()

    return profile_list

def ProfileMostProbableKmer(text, k, profile):
    n = len(text)
    kmer_list = []
    pair_list = []
    probability_list = []
    for i in range(n-k+1):
        kmer = text[i:i + k]
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

def GreedyMotifSearch(Dna, k, t):
    n = len(Dna[0])
    best_motifs = []


    for text in Dna:
        best_motifs.append(text[0:k])


    for i in range(n-k+1):
        motif_list = []
        motif_list.append(Dna[0][i:i+k])
        for j in range(1,t):
            profile = Profile(motif_list)
            probkmer = ProfileMostProbableKmer(Dna[j], k, profile)
            motif_list.append(probkmer)
        if Score(motif_list) <= Score(best_motifs):
            best_motifs = motif_list
    return best_motifs


def count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)
    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def profile(Motifs):
    t = len(Motifs)
    k = len(Motifs[0])
    profile = {}
    profile = count(Motifs)
    for symbol in 'ACGT':
        for j in range(k):
            profile[symbol][j] = profile[symbol][j] / float(t)
    return profile


def consensus(Motifs):
    k = len(Motifs[0])
    counts = count(Motifs)
    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if counts[symbol][j] > m:
                m = counts[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def score(Motifs):
    profile = count(Motifs)
    Consensus = consensus(Motifs)
    t = len(Motifs)
    score = 0
    for i in range(len(Motifs[0])):
        score = score + (t - profile[Consensus[i]][i])
    return score


def pr(Text, Profile):
    pr = 1
    for i in range(len(Text)):
        pr = pr * Profile[Text[i]][i]
    return pr


def profile_most_probable_pattern(Text, Profile):
    T = len(Text)
    K = len(Profile['A'])
    prob = 0
    x = Text[0:K]
    for i in range(T - K + 1):
        Subtext = Text[i:i + K]
        temp_prob = pr(Subtext, Profile)
        if temp_prob > prob:
            prob = temp_prob
            x = Subtext
    return x


def greedy_motif_search(Dna, k, t):
    BestMotifs = []
    for i in range(0, t):
        BestMotifs.append(Dna[i][0:k])
    n = len(Dna[0])
    for i in range(n - k + 1):
        Motifs = []
        Motifs.append(Dna[0][i:i + k])
        for j in range(1, t):
            P = profile(Motifs[0:j])
            Motifs.append(profile_most_probable_pattern(Dna[j], P))
        if score(Motifs) < score(BestMotifs):
            BestMotifs = Motifs
    return BestMotifs

print(greedy_motif_search(Dna, k, t))



