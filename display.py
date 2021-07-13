import sys
from console.screen import sc

class ConsoleDisplay():
    def __init__(self):
        pass

    def display_grid(self, grid: list):
        with sc.location(0, 0):
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if(cell):
                        print("X", end = "")
                    else:
                        print("0", end="")
                print("")
