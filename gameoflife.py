from display import ConsoleDisplay
from iterate import fetch_live_neighbors, iterate
from input_handler import read_grid_from_file
import time
import argparse

parser = argparse.ArgumentParser(description="Simulate conway's game of life.")
parser.add_argument("path", type=str, default="grid.txt", nargs='?')
parser.add_argument("iterations", type=int, default=1000, nargs='?')

args = parser.parse_args()

grid = read_grid_from_file(args.path)
display = ConsoleDisplay()

for i in range(args.iterations):
    display.display_grid(grid)
    time.sleep(0.03)
    grid = iterate(grid)