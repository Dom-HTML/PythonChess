class Board:
    def __init__(self):
        self.symb = ["♟","♘","♗","♖","♕","♔"]
        self.pieces = []

        self.board = {}
        self.sPat = "31254213"

        self.reset()

    def reset(self):
        board = {}
        letter = ""
        number = 1
        
        for i in range(8):
            number = 8 - i
            for j in range(8):
                letter = chr(j + 97)
                key = f"{letter}{number}"
                colour = "B"
                typ = "B"
                if number > 6:
                    typ = "W"
                    colour = "W"
                if number == 7 or number == 2:
                    typ = typ + self.symb[0]
                elif number == 8 or number == 1:
                    index = self.sPat[j]
                    typ = typ + self.symb[int(index)]
                elif 6 <= number or number >= 3:
                    board[key] = None
                    continue
                
                newPiece = Piece(typ, colour)
                newPiece.updatePos(key)
                self.pieces.append(newPiece)
                board.update({key:newPiece})

        self.board = board

    def placeholder(self, piece):
        ph = str(self.symb[piece.typIndex])+piece.colour
        return ph

    def concatPos(self, dic):
        coord = str(dic["x"]) + str(dic["y"])
        return coord

    def updateBoard(self): #will loop piece array and update piece positions
        board = {}
        letter = ""
        number = 1
        
        for i in range(8):
            number = 8 - i
            for j in range(8):
                letter = chr(j + 97)
                key = f"{letter}{number}"
                board[key] = None

        for piece in self.pieces:
            lastPos = self.concatPos(piece.lastPos)
            curPos = self.concatPos(piece.pos)

            board[lastPos] = None
            board[curPos] = piece

        self.board = board

    def tileInfo(self): # output the info of tile eg what piece on it
        pass

    def play(self):
        print("Playing...")
        playing = True
        start = True
        while playing:
            if start:
                self.outBoard()
                start = False
            p = str(input("piece: ")).lower()
            m = str(input("move: ")).lower()
            print(self.board[p])
            print(f"piece:{p}, move:{m}")
            self.board[p].updatePos(m)
            self.updateBoard()
            self.outBoard()

    def outBoard(self):#output board graphically for player to view
        print("outputting board")
        line = ""
        letter = ""
        number = 1
        
        for i in range(8):
            number = 8 - i
            line = ""
            for j in range(8):
                letter = chr(j + 97)
                key = f"{letter}{number}"
                piece = self.board[key]
                if piece == None:
                    line = line + "E♖"
                else:
                    typ = piece.getType()
                    line = line + typ
            print(line)

class Piece:
    def __init__(self, typ = "Eᴥ", colour = "Nu"):
        self.pos = {"x":"A", "y":1}
        self.typ = typ
        self.colour = colour
        self.lastPos = None
            
    def updatePos(self, coord): #example data: C4
        self.lastPos = self.pos
        self.pos[f"x"] = coord[0]
        self.pos[f"y"] = coord[1]

    def getType(self):
        return self.typ

class Grid:
    def __init__(self, sizeX, sizeY, cellSize):
        self.chars = {"corn":["┏","┓","┗","┛"], "edge":["•","┣","┫","┳","┻","╋","┃"], "space":[" "]}
        self.grid = []
        self.sizeX = sizeX#• 
        self.sizeY = sizeY#━
        self.cellSize = cellSize

        self.build()

    def build(self, array = []):
        corn = self.chars["corn"]
        edge = self.chars["edge"]
        space = self.chars["space"]
        line = ""
        for i in range(self.sizeY+1):
            line = ""
            if i == 0:
                line = corn[0]+(self.sizeX-1)*((self.cellSize*edge[0])+edge[3])+self.cellSize*edge[0]+corn[1]
            elif i == self.sizeY:
                for y in range(self.cellSize):
                    spaceLine = edge[6]+(self.sizeX-1)*(self.cellSize*space[0]+edge[6])+self.cellSize*space[0]+edge[6]
                    self.grid.append(spaceLine)
                line = corn[2]+(self.sizeX-1)*((self.cellSize*edge[0])+edge[4])+self.cellSize*edge[0]+corn[3]
            elif i > 0:
                for y in range(self.cellSize):
                    spaceLine = edge[6]+(self.sizeX-1)*(self.cellSize*space[0]+edge[6])+self.cellSize*space[0]+edge[6]
                    self.grid.append(spaceLine)
                line = edge[1]+(self.sizeX-1)*((self.cellSize*edge[0])+edge[5])+self.cellSize*edge[0]+edge[2]

            self.grid.append(line)

    def out(self):
        for line in self.grid:
            print(line)

thisGame = Board()
thisGame.play()

#while True:
    #x = int(input("x: "))
    #y = int(input("y: "))
    #cell = int(input("cell: "))
    #myGrid = Grid(x, y, cell)
    #myGrid.out()
        
