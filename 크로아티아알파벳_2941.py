word = ['c=','c-','dz=','d-','lj','nj','s=','z=']
sentence = input()

for i in range (len(word)):
    sentence=sentence.replace(word[i],'a')

print(sentence)