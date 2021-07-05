from iterate import fetch_live_neighbors, iterate

grid = [[False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False], [False, False, False, False, False]]
grid[1][2] = True
grid[2][2] = True
grid[3][2] = True

print(fetch_live_neighbors(grid, (2, 1)))


#print(grid)
grid = iterate(grid)
print(grid)
grid = iterate(grid)
print(grid)
grid = iterate(grid)
print(grid)
grid = iterate(grid)
print(grid)
