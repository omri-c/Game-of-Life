import sys

def display_grid(grid: list):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if(cell):
                print("X", end="")
            else:
                print("0", end="")
        print("\r")
