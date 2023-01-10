# Minimum Skew Problem

def CountG(seq):
    count = 0
    for nuc in seq:
        if nuc == 'G':
            count = count + 1
    return(count)

def CountC(seq):
    count = 0
    for nuc in seq:
        if nuc == 'C':
            count = count + 1
    return(count)

def Skew(i, text):
    k = 0
    result = []
    while k < i + 1:
        window = text[:k]
        G_number = CountG(window)
        C_number = CountC(window)
        GCdiff = int(G_number) - int(C_number)
        result.append(str(GCdiff))
        k = k + 1
    print(result)

sequence = input('Enter Sequence: ')

def skew(sequence):
    c = 0
    g = 0
    min_skew = 0
    skew_list = []
    index = 0
    for i in sequence:
        index += 1
        if i == 'C':
            c += 1
        if i == 'G':
            g += 1
        skew = g-c
        if skew < min_skew:
            skew_list = [index]
            min_skew = skew
        if skew == min_skew and index not in skew_list:
            skew_list.append(index)
    print(skew_list)

skew(sequence)

