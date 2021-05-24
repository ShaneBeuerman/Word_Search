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
                arr[i][j] = random.choice(string.ascii_lowercase)

def buttonPress(char):
    global currentLetters
    currentLetters += char
    print(currentLetters)
    updateGUI()

def crossOff():
    print("To be continued")

def win():
    print("N/A")

def updateGUI():
    global letterslabel
    letterslabel.config(text="Current Letters: " + "\n" + currentLetters)

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
buttons =  [[None]*10 for _ in range(10)]
currentLetters = ""
for i in range(10):
    for j in range(10):
        letter = board[j][i]
        button = tkinter.Button(top, text=letter, command = lambda cur=letter: buttonPress(cur))
        buttons[j][i] = button
        buttons[j][i].grid(row = j, column = i)
words = []
for i in range(len(wordlist)):
    word = tkinter.Label(text=wordlist[i])
    words.append(word)
    word.grid(column = 11, row = i)

letterslabel = tkinter.Label(text="Current letters: " + "\n" + currentLetters)
letterslabel.grid(column = 12, row = 0)

top.mainloop()