#Reverese Complement Problem
text = input('Enter Text: ')

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
    print(patternRC)

RevComp(text)
