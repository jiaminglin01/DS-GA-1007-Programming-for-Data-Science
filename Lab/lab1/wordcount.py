# Read a song from file 
song = open("lyrics.txt","r")
word = input("Type your favorite word: ")
d = {word: 0}
for line in song:
    if word in line:
        d[word] += line.count(word)
print('\n The word \"{}\" appears {} times in this song'.format(word, d[word]))
