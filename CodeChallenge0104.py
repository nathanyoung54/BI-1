#Pattern Matching Problem
pattern = input('Enter Pattern: ')
text = input('Enter Text: ')

def StartingPoints(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)
    points = ''
    for i in range(text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            points = points + str(i) + ' '
    print(points)

StartingPoints(text, pattern)