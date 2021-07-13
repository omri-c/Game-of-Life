import sys

def display_grid(grid: list):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if(cell):
                sys.stdout.write("X")
            else:
                sys.stdout.write("0")
        sys.stdout.write("\n")

def flush_screen():
    sys.stdout.flush()