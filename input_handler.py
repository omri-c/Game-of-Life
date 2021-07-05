def read_grid_from_file(path: str) -> list:
    grid = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for l in lines:
            l = l.split(",")
            new_line = []
            for i in l:
                if(i == 0):
                    new_line.append(False)
                else:
                    new_line.append(True)
            grid.append(new_line)
        
    return grid