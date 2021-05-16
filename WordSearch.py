#Word Search
import tkinter
import random
import string
import time
from tkinter import *
board = []
wordlist = []

def printArray(arr):
    for i in arr:
        print(i)

def fillSpacesWithRandomLetters(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '-':
                arr[i][j] = random.choice(string.ascii_letters)                

f = open("wordSearch.txt", "r")
while(True):
    line = f.readline()
    if not line:
        break
    line = line.strip("\n")
    line = line.replace(" ", "")
    board.append(list(line))
printArray(board)
fillSpacesWithRandomLetters(board)
printArray(board)
f = open("wordList.txt", "r")
while(True):
    line = f.readline()
    if not line:
        break
    line = line.strip("\n")
    wordlist.append(line)
printArray(wordlist)

top = tkinter.Tk()
buttons = []
for i in range(10):
    for j in range(10):
        button = tkinter.Button(top, text=board[j][i])
        buttons.append(button)
        button.grid(row = j, column = i)
top.mainloop()