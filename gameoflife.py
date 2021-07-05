from iterate import fetch_live_neighbors, iterate
from input_handler import read_grid_from_file


grid = read_grid_from_file("grid.txt")

grid = iterate(grid)
print(grid)
grid = iterate(grid)
print(grid)
grid = iterate(grid)
print(grid)
grid = iterate(grid)
print(grid)
