wrdray = []

#Search function
#Find the position of a word in the main word array
def wrdfnd(wrd):
    for i in range(len(wrdray)):
        nxtwrd = wrdray[i]
        if nxtwrd == wrd:
            return i
    return -1

#Adds missing words to word array
#Returns 1 if missing word was added
#returns 0 if word was already in word array
def addwrd(wrd):
    if wrdfnd(wrd) == -1:
        wrdray.append(wrd)
        return 1
    else:
        return 0

f = open("words.txt")

#Reads the main words.txt file and loads each word into the wrdray
while next != "":
    next = f.readline().rstrip()
    wrdray.append(next)

