import os
import platform
import random
import time

All_Cells = []

ROW,COLM = (32,32)

class Cell_class:
    def __init__(self, x, y ,):
        self.x = x
        self.y = y
        self.neigbours = 0
        self.alive = False
        self.nextIt = False

    def count_neighbours(self):
        OFFSET = [
            [-1, -1],[-1, 0],[-1, 1],
            [ 0, -1],        [ 0, 1],
            [ 1, -1],[ 1, 0],[ 1, 1]
        ]
        self.neigbours = 0
        for dx, dy in OFFSET:
            neighbor_x = self.x + dx
            neighbor_y = self.y + dy
            if 0 <= neighbor_x < ROW and 0 <= neighbor_y < COLM:
                neighbor_cell = All_Cells[neighbor_x][neighbor_y]
                if neighbor_cell.alive:
                    self.neigbours += 1
    def check_rules(self):
        if(self.alive):
            if(self.neigbours < 2 or self.neigbours > 3):
                self.nextIt = False
        else:
            if(self.neigbours == 3):
                self.nextIt = True
    def apply_rules(self):
        self.alive = self.nextIt

def display():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    for i in range(ROW):
        screen = ""
        for j in range(COLM):
            if(All_Cells[i][j].alive):
                screen += "■ "
            else:
                screen += "□ "
        print(screen)

def create():
    for i in range(ROW):
        subcells = []
        for j in range(COLM):
            cell = Cell_class(i,j)
            subcells.append(cell)
        All_Cells.append(subcells)

def randomize_grid():
    for i in range(ROW):
        for j in range(COLM):
            All_Cells[i][j].alive = bool(random.randint(0, 1))

        

create()

randomize_grid()

while True:
    for i in range(ROW):
        for j in range(COLM):
            All_Cells[i][j].count_neighbours()
            All_Cells[i][j].check_rules()
    for i in range(ROW):
        for j in range(COLM):
            All_Cells[i][j].apply_rules()
    display()
    time.sleep(1)