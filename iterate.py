def iterate(grid: list) -> list:
    #Foreach cell:
        # If alive:
            # If (live_neighbors is 2 or 3):
                #alive
            # else:
                #dead
        # else:
            # if(live_neighbors is 3):
                # alive
            # else:
                # dead 
    a = 0

def fetch_live_neighbors(grid: list, index: tuple) -> int:
    neighbor_indices = []
    live_neighbors = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            neighbor_indices.append((index[0] + i, index[1] + j))
            # remove the current cell from list of indices
            neighbor_indices.remove((i, j))

    for i in neighbor_indices:
        try:
            if(grid[i[0]][i[1]] == True):
                live_neighbors += 1
        except IndexError:
            # This is expected as on edge cells we will go out of bounds.
            # ToDo: might be smarter to handle it better, as hiding an expected exception might hide undesired behaviour. 
            pass
    
    return live_neighbors