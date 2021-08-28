import tkinter as tk
from enum import Enum
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

def genRandomColor():
    """
    @returns a random string representing a color
    """
    r = random.randint(1,4)

    match r:
        case 1:
            return Color.RED.value
        case 2:
            return Color.GREEN.value
        case 3:
            return Color.BLACK.value
        default:
            return Color.WHITE.value

#-----------------------------------
#       Colors Enum
#-----------------------------------
class Color(Enum):
     RED = "red"
     GREEN = "green"
     BLACK = "black"
     WHITE = "white" 

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
        self.content.grid(column=0,row=0,columnspan=self.width,
                        rowspan=self.height)
        #adds pixels
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
                board[row][col] = self._createPixel(row, col)
        self.board = board
    
    def _createPixel(self, row : int, col : int):
        """
        @return: an instance of a label
        """
        label = tk.Label(self.content, 
                        bg= genRandomColor(), 
                        width = 2*_PIXELsize, 
                        height = 1*_PIXELsize)
        label.grid(column=col*_PIXELsize, 
                    row=row*_PIXELsize,
                    columnspan=_PIXELsize,
                    rowspan=_PIXELsize)
        return label
    
    def setPixel(self, i : int, j : int, color):
        """
        Set the color of pixel i,j.
        @param i,j: pixel indexes on board
        @param color: new pixel color
        """
        if i < self.height and j < self.width:
            self.board[i][j].config(bg = color.value)
        else:
            print(f"Error setting color pixel {i},{j}\nIndex out of range")

if __name__=="__main__":
    gameScreen = Screen(_WIDTH, _HEIGHT)
    for i in range(_WIDTH):
        gameScreen.setPixel(0,i,Color.RED)
    gameScreen.start()
