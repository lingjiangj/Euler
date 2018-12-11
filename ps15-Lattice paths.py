# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

# How many such routes are there through a 20×20 grid?

def Lattice_paths(grid):
    lattice = {}
    #only one way to get to each of these points in first row,mark those points with 1
    #only one way to get to each of these points in first column,mark those points with 1
    for r in range(0,grid+1):
        for c in range(0,grid+1):
            lattice[(c,0)] = 1
            lattice[(0,r)] = 1
    #start from (1,1),add the above mark and left mark of the points
    for i in range(1, grid+1):
        for j in range(1,grid+1):
            lattice[(i,j)] = lattice[(i-1,j)] + lattice[(i,j-1)]
    
    return lattice[(grid,grid)]

print(Lattice_paths(20))
