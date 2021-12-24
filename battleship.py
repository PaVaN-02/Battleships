"""
Battleship Project
Name:
Roll No:
"""

import battleship_tests as test

project = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["rows"]=10
    data["cols"]=10
    data["board_size"]=500
    data["cell_size"]=(int)(data["board_size"]/(data["rows"]*data["cols"]))
    data["num_ships"]= 5
    data["tempShip"]=[]
    data["userShips"]=0
    data["winner"]=None
    data["maxturns"]=100
    data["currentturns"]=0
    data["compboard"]=emptyGrid(data["rows"],data["cols"])
    data["userboard"]=emptyGrid(data["rows"], data["cols"])
    data["compboard"]=addShips(data["compboard"],data["num_ships"])
    return data

'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, compCanvas,data["compboard"] ,False)
    drawGrid(data, userCanvas,data["userboard"], True)
    drawShip(data, userCanvas, data["tempShip"])
    drawGameOver(data, userCanvas)
    drawGameOver(data, compCanvas)
    return None

'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
     if  event.keysym == 'Return':
 
        makeModel(data)
        return False 


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    if data["winner"]!=None:
        return None
    rc = getClickedCell(data, event)
    if(board=="user"):
        clickUserBoard(data, rc[0], rc[1])
    else:
        runGameTurn(data, rc[0], rc[1])

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    row=[]
    for i in range (rows):
        col=[]
        for j in range(cols):
            col.append(EMPTY_UNCLICKED)
        row.append(col)    

    return row

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    import random
    row = random.randint(1,8)
    col = random.randint(1,8)
    hv = random.randint(0,1)
    if hv==0:
      p=row-1
      randomValue=col
    else:
      p=col-1
      randomValue=row
    d1=[[randomValue for j in range(1)] for i in range(3)]

    for i in range(len(d1)):
      d2=d1[i]
 
      d2.insert(hv,p)
      p=p+1
    
    return d1



'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    count=0
    for i in range(3):
        row=ship[i][0]
        col=ship[i][1]
        if grid[row][col]==EMPTY_UNCLICKED:
           count=count+1
    if count==3:
        return True
    else:
       return False

'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    count=0
    while count < numShips:
        ship = createShip()  
        check =checkShip(grid,ship)
        if check :
            for i in ship:
               row=i[0]
               col=i[1]
               grid[row][col]=SHIP_UNCLICKED
            count=count+1
            
    return grid


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
        for i in range(data["rows"]):
            for j in range(data["cols"]):
               if grid[i][j]==SHIP_UNCLICKED:
                   if showShips :
                      canvas.create_rectangle(j*data["cols"]*data["cell_size"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="yellow")
                   else:
                      canvas.create_rectangle(j*data["cols"]*data["cell_size"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="blue")
               elif (grid[i][j]==SHIP_CLICKED):
                      canvas.create_rectangle(j*data["cols"]*data["cell_size"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="red")
                    
               elif (grid[i][j]==EMPTY_CLICKED):
                      canvas.create_rectangle(j*data["cols"]*data["cell_size"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="white")    
               else:
                  canvas.create_rectangle(j*data["cols"]*data["cell_size"], i*data["rows"]*data["cell_size"], (j+1)*data["cols"]*data["cell_size"], (i+1)*data["rows"]*data["cell_size"],fill="blue")
        canvas.pack()    

### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    row=[]
    col=[]
    for i in range(len(ship)):
        row.append(ship[i][0])
        col.append(ship[i][1])
    count=0
    truecount=0
    c=col[0]
    for i in range(1,len(ship)):
        if(c==col[i]):
           count=count+1
    if count==len(ship)-1:
       truecount=truecount+1  
 
    row.sort()
    count=0
    for i in range (len(ship)-1):
        if (row[i]+1==row[i+1]):
          count=count+1
    if (count==len(ship)-1):
        truecount=truecount+1  
    if truecount==2:
        return True
    else:
        return False  


'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    row=[]
    col=[]
    for i in range(len(ship)):
        row.append(ship[i][0])
        col.append(ship[i][1])
    count=0
    truecount=0
    r=row[0]
    for i in range(1,len(ship)):
        if(r==row[i]):
           count=count+1
    if count==len(ship)-1:
       truecount=truecount+1  
 
    col.sort()
    count=0
    for i in range (len(ship)-1):
        if (col[i]+1==col[i+1]):
          count=count+1
    if (count==len(ship)-1):
        truecount=truecount+1  
    if truecount==2:
        return True
    else:
        return False    

'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    l=[]
    i=(int)(event.y/(data["cols"]*data["cell_size"]))
    j=(int)(event.x/(data["rows"]*data["cell_size"]))
    l.append(i)
    l.append(j)
    return l


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    print(ship)     
    for i in range(len(ship)):
        x=ship[i][0]
        y=ship[i][1]
        canvas.create_rectangle(y*data["cols"]*data["cell_size"], x*data["rows"]*data["cell_size"], (y+1)*data["cols"]*data["cell_size"], (x+1)*data["rows"]*data["cell_size"],fill="white")
    return None


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    flag=count=0
    if(len(ship)==3):
        flag=flag+1
    v=isVertical(ship)
    h=isHorizontal(ship)
 
    if(checkShip(grid,ship)&((h)|(v)==True)):
        flag=flag+1
 
    for i in range (len(ship)):
      row=ship[i][0]
      col=ship[i][1]
      if(grid[row][col]!=SHIP_UNCLICKED):
           count=count+1
    if (count==len(ship)):
        flag=flag+1
    if(flag==3):
        return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if(shipIsValid(data["userboard"],data["tempShip"])):
        for i in range (len(data["tempShip"])):
           row=data["tempShip"][i][0]
           col=data["tempShip"][i][1]
           data["userboard"][row][col]=SHIP_UNCLICKED
        data["userShips"]=data["userShips"]+1
    else:
        print("ship is not valid")
    data["tempShip"]=[]
    return None


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    if(data["userShips"]==data["num_ships"]):
        return None
    t=[row,col]
    for k in range(len(data["tempShip"])):
      if (data["tempShip"][k]==t):
           return None
    data["tempShip"].append(t)
 
    if(len(data["tempShip"])==3):
        placeShip(data)
    if(data["userShips"]==data["num_ships"]):
        print("you can start the game")
    return None


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if (board[row][col]==SHIP_UNCLICKED):
        board[row][col]=SHIP_CLICKED
    if (board[row][col]==EMPTY_UNCLICKED):    
        board[row][col]=EMPTY_CLICKED
    if (isGameOver(board)==True):
        data["winner"]=player
    return None


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    if ((data["compboard"][row][col] == SHIP_CLICKED) or (data["compboard"][row][col] == EMPTY_CLICKED)):
      return  None
    else:
        updateBoard(data, data["compboard"], row, col, "user")
    [r,c]=getComputerGuess(data["userboard"])
    updateBoard(data, data["userboard"], r, c, "comp")
    data["currentturns"]=data["currentturns"]+1
    if (data["currentturns"]==data["maxturns"]):
        data["winner"]="Draw"

'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    randomrowvalue = random.randint(0,9)
    randomcolvalue = random.randint(0,9)
    while ((board[randomrowvalue][randomcolvalue] == SHIP_CLICKED) or (board[randomrowvalue][randomcolvalue]==EMPTY_CLICKED)):
        randomrowvalue = random.randint(0,9)
        randomcolvalue = random.randint(0,9)  
    return [randomrowvalue,randomcolvalue]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range (len(board)):
        for j in range(len(board[i])):
            if board[i][j]== SHIP_UNCLICKED:
                return False
    return True
'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if (data["winner"]=="user"):
        canvas.create_text(250, 150, text="CONGRATULATIONS!", fill="gold", font=('italic 30 bold'))
        canvas.create_text(250, 250, text="PRESS ENTER TO REPLAY", fill="black", font=('italic 15 bold'))
    if (data["winner"]=="comp"):
        canvas.create_text(250, 150, text="YOU LOST!", fill="brown", font=('italic 30 bold'))
        canvas.create_text(250, 250, text="PRESS ENTER TO REPLAY", fill="black", font=('italic 15 bold'))
    if (data["winner"]=="Draw"):
        canvas.create_text(250, 150, text="OUT OF MOVES!", fill="silver", font=('italic 30 bold'))
        canvas.create_text(250, 250, text="PRESS ENTER TO REPLAY", fill="black", font=('italic 15 bold')) 
    canvas.pack()
    return None


### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = { }
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text = "USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text = "COMPUTER BOARD - click to make guesses. The computer will guess on your board.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event : keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event : mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    test.testEmptyGrid()
    test.testCreateShip()
    test.testCheckShip()
    test.testAddShips()
    test.testMakeModel()
    test.testDrawGrid()
    test.testIsVertical()
    test.testIsHorizontal()
    test.testGetClickedCell()
    test.testDrawShip()
    test.testShipIsValid()
    test.testUpdateBoard()
    test.testGetComputerGuess()
    test.testIsGameOver()
    test.testDrawGameOver()


    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
