#Word Search
import tkinter
import random
import string
import time
from tkinter import *
board = []
wordlist = []
buttonsPressed = []
direction = ""
currentLetters = ""

def printArray(arr):
    for i in arr:
        print(i)

def fillSpacesWithRandomLetters(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == '-':
                arr[i][j] = random.choice(string.ascii_lowercase)

def buttonPress(row, col, char):
    global currentLetters
    global board
    global buttonsPressed
    global direction
    if len(currentLetters) == 0:
        currentLetters += char.capitalize()
        pair = (row, col)
        buttonsPressed.append(pair)
    if len(currentLetters) == 1:
        pair = buttonsPressed[0]
        if pair[0] == row+1:
            if pair[1] == col+1:
                direction += "NW"
            elif pair[1] == col:
                direction += "N"
            elif pair[1] == col-1:
                direction += "NE"
        elif pair[0] == row:
            if pair[1] == col+1:
                direction += "W"
            elif pair[1] == col-1:
                direction += "E"
        elif pair[0] == row-1:
            if pair[1] == col+1:
                direction += "SW"
            elif pair[1] == col:
                direction += "S"
            elif pair[1] == col-1:
                direction += "SE"
        if len(direction) >= 1:
            currentLetters += char.capitalize()
            pair = (row, col)
            buttonsPressed.append(pair)
    if len(currentLetters) > 1:
        lastPoint = buttonsPressed[len(buttonsPressed)-1]
        confirm = False
        if direction == "S" and lastPoint[0] == row-1 and lastPoint[1] == col:
            confirm = True
        elif direction == "N" and lastPoint[0] == row+1 and lastPoint[1] == col:
            confirm = True
        elif direction == "NE" and lastPoint[0] == row+1 and lastPoint[1] == col-1:
            confirm = True
        elif direction == "NW" and lastPoint[0] == row+1 and lastPoint[1] == col+1:
            confirm = True
        elif direction == "SE" and lastPoint[0] == row-1 and lastPoint[1] == col-1:
            confirm = True
        elif direction == "SW" and lastPoint[0] == row-1 and lastPoint[1] == col+1:
            confirm = True
        elif direction == "W" and lastPoint[0] == row and lastPoint[1] == col+1:
            confirm = True
        elif direction == "E" and lastPoint[0] == row and lastPoint[1] == col-1:
            confirm = True
        if confirm:
            currentLetters += char.capitalize()
            pair = (row, col)
            buttonsPressed.append(pair)
    updateGUI()

def clearLetters():
    global currentLetters
    global buttonsPressed
    global direction
    buttonsPressed.clear()
    currentLetters = ""
    direction = ""
    updateGUI()

def win():
    global wordlist
    for i in wordlist:
        if i != "":
            return
    winScreen = tkinter.Tk()
    winScreen.wm_title("Congratulations")
    winLabel = tkinter.Label(winScreen, text="You won")
    winButton = tkinter.Button(winScreen, text="Okay", command=winScreen.destroy)
    winLabel.pack()
    winButton.pack()
    winScreen.mainloop()

def updateGUI():
    global letterslabel
    global currentLetters
    global wordlist
    global words
    global direction
    letterslabel.config(text="Current Letters: " + "\n" + currentLetters)
    for i in range(len(wordlist)):
        if wordlist[i] == currentLetters:
            words[i].config(text= "")
            wordlist[i] = ""
            currentLetters = ""
            direction = ""
            buttonsPressed.clear()
            letterslabel.config(text="Current Letters: " + "\n" + currentLetters)
    win()
            

f = open("wordSearch.txt", "r")
while(True):
    line = f.readline()
    if not line:
        break
    line = line.strip("\n")
    line = line.replace(" ", "")
    board.append(list(line))
fillSpacesWithRandomLetters(board)
f = open("wordList.txt", "r")
while(True):
    line = f.readline()
    if not line:
        break
    line = line.strip("\n")
    wordlist.append(line)

top = tkinter.Tk()
top.wm_title("Word Search")
buttons =  [[None]*10 for _ in range(10)]

for i in range(10):
    for j in range(10):
        letter = board[j][i]
        button = tkinter.Button(top, text=letter, command = lambda cur=letter,row=j,col=i: buttonPress(row, col, cur))
        buttons[j][i] = button
        buttons[j][i].grid(row = j, column = i)
words = []
for i in range(len(wordlist)):
    word = tkinter.Label(text=wordlist[i])
    words.append(word)
    word.grid(column = 11, row = i)

letterslabel = tkinter.Label(text="Current letters: " + "\n" + currentLetters)
letterslabel.grid(column = 12, row = 0)
clearButton = tkinter.Button(text="Clear currentLetters", comman = clearLetters)
clearButton.grid(column =12, row = 1)

top.mainloop()