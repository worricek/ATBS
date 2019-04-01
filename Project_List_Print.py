def ListFormat(words):
    for i in range(0, len(words)):
        if i == len(words)-1:
            break
        else:
            print(words[i])
    print('and ' + words[i])

words=[]
while True:
    print('Enter word ' + str(len(words) +1) + ':')
    wordx=input()
    if wordx=='':
        break
    words=words+[wordx]
print('The words are:')
for wordx in words:
    print('    ' + wordx)
ListFormat(words)
