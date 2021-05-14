#Word Search

board = []
wordlist = []

def printArray(arr):
    for i in arr:
        print(i)

f = open("wordSearch.txt", "r")
while(True):
    line = f.readline()
    if not line:
        break
    line = line.strip("\n")
    board.append(line)
printArray(board)
f = open("wordList.txt", "r")
while(True):
    line = f.readline()
    if not line:
        break
    line = line.strip("\n")
    wordlist.append(line)
printArray(wordlist)

    
