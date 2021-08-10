import sys
import tkinter as tk
from typing import DefaultDict
import random

#-----------------------------------
#       Definitions
#-----------------------------------
_WIDTH = 20                #in pixels
_HEIGHT = 30              #in pixels
_DEFAULTCOLOR = "red"     #rabcdom value
_DEFAULTVAL = -1            #radom value
_PIXELsize = 1

#-----------------------------------
#       Helper functions
#-----------------------------------
def generateEmptyBoard(x,y):
    return [[_DEFAULTVAL for j in range(x)] for i in range(y)]

def genDimensions(x , y, Default = False):
    xtag = x*_PIXELsize
    ytag = y*_PIXELsize*10
    dim = "500x500" if Default else f"{str(xtag)}x{str(ytag)}"
    return dim

def genRandomColor():
    r=  random.randint(1,4)

    if r == 1:
        return "red"
    if r == 2:
        return "green"
    if r == 3:
        return "black"
    return "white"
    

#-----------------------------------
#       Class Screen
#-----------------------------------
class Screen(tk.Frame):
    def __init__(self, width : int, height : int):
        #Init Tkinter
        self.root = tk.Tk()
        super().__init__(self.root)
        #----------------
        self.width = width
        self.height = height

        self.content = tk.Frame(self.root)
        frame = tk.Frame(self.content, 
                        borderwidth=10, 
                        relief="ridge")
        self.content.grid(column=0,row=0,columnspan=self.width,
                        rowspan=self.height)
        frame.grid(column=0, 
                    row=0, 
                    columnspan=self.width, 
                    rowspan=self.height)

        self._initScreen()

    def start(self):
        self.root.mainloop()

    def _initScreen(self):
        """
        creates a matrix of size _WIDTH*_HEIGHT initialized with lables
        @return: the initialized matrix
        """
        board = generateEmptyBoard(self.width,self.height)
        for row in range(self.height):
            for col in range(self.width):
                board[row][col] = self._createPixel(row, col, genRandomColor())
        self.board = board
    
    def _createPixel(self, row, col, default_color):
        """
        @return: an instance of a label
        """
        label = tk.Label(self.content, 
                        bg=default_color, 
                        width = 2*_PIXELsize, 
                        height = 1*_PIXELsize)
        label.grid(column=col*_PIXELsize, 
                    row=row*_PIXELsize,
                    columnspan=_PIXELsize,
                    rowspan=_PIXELsize)
        return label

if __name__=="__main__":
    gameScreen = Screen(_WIDTH, _HEIGHT)
    gameScreen.start()