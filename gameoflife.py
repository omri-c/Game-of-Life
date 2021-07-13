from display import display_grid
from iterate import fetch_live_neighbors, iterate
from input_handler import read_grid_from_file
import time

grid = read_grid_from_file("grid.txt")
display_grid(grid)
time.sleep(0.1)
grid = iterate(grid)
display_grid(grid)
time.sleep(0.1)
grid = iterate(grid)
display_grid(grid)
time.sleep(0.1)
grid = iterate(grid)
display_grid(grid)
time.sleep(0.1)
grid = iterate(grid)
display_grid(grid)
