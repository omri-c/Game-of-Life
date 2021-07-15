def read_grid_from_file(path: str) -> list:
    grid = []
    with open(path, 'r') as f:
        lines = f.readlines()
        for l in lines:
            #l = l.split(",")
            new_line = [(x in ('1', '1\n')) for x in l]
            grid.append(new_line)
        
    return grid