from iterate import fetch_live_neighbors

grid = [[False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, 
False, False, False], [False, False, False, False, False, False, False, False, False, False], [False, False, False, False, False, False, False, False, False, False]]
print(grid)
grid[1][1] = True
grid[1][2] = True
grid[1][3] = True


print(fetch_live_neighbors(grid, (0,1)))
assert fetch_live_neighbors(grid, (0,1)) == 2