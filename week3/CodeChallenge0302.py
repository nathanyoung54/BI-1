from collections import Counter

import numpy as np

Motifs = [
"TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"
]
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

def Count(Motifs):
    # returns a matrix showing number of A, C, G, T

    Motifs_arr = np.array([list(seq) for seq in Motifs])
    count_matrix = np.zeros((4, Motifs_arr.shape[1]))

    for i in range(Motifs_arr.shape[1]):
        column_i = Motifs_arr[:, i]
        # columns
        len_column_i = column_i.shape[0]
        # length of column = 10
        count = Counter(column_i)
        count_matrix[0, i] = count["A"]
        count_matrix[1, i] = count["C"]
        count_matrix[2, i] = count["G"]
        count_matrix[3, i] = count["T"]
    return count_matrix


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

    return profile_matrix

profile = [
        [0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
        [0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
        [0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
        [0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4] ]


import math
sum1 = -(0.2* math.log(0.2, 2) + 0.1* math.log(0.1, 2) + 0.7* math.log(0.7, 2))
sum2 = -(0.2* math.log(0.2, 2) + 0.6* math.log(0.6, 2) + 0.2* math.log(0.2, 2))
sum3 = -(1.0* math.log(1.0, 2))
sum4 = -(1.0* math.log(1.0, 2))
sum5 = -(0.9* math.log(0.9, 2) + 0.1* math.log(0.1, 2))
sum6 = -(0.9* math.log(0.9, 2) + 0.1* math.log(0.1, 2))
sum7 = -(0.9* math.log(0.9, 2) + 0.1* math.log(0.1, 2))
sum8 = -(0.1* math.log(0.1, 2) + 0.4* math.log(0.4, 2) + 0.5* math.log(0.5, 2))
sum9 = -(0.1* math.log(0.1, 2) + 0.1* math.log(0.1, 2) + 0.8* math.log(0.8, 2))
sum10 = -(0.1* math.log(0.1, 2) + 0.2* math.log(0.2, 2) + 0.7* math.log(0.7, 2))
sum11 = -(0.3* math.log(0.3, 2) + 0.4* math.log(0.4, 2) + 0.3* math.log(0.3, 2))
sum12 = -(0.6* math.log(0.6, 2) + 0.4* math.log(0.4, 2))
SUM = sum1+sum2+sum3+sum4+sum5+sum6+sum7+sum8+sum9+sum10+sum11+sum12
print(SUM)
print(sum2)




print(Score(Motifs))
print(Count(Motifs))
print(Profile(Motifs))








