# Hamming Distance Problem

p = input('Enter p: ')
q = input('Enter q: ')

def HammingDistance(p, q):
    length = len(p)
    z = 0
    for n in range(length):
        if p[n] != q[n]:
            z = z + 1
    return(z)

print(HammingDistance(p, q))