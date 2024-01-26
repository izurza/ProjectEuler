## Problem 18

directions = [(0,1),(1,1)]
triangle = [[3, 0, 0, 0], [7, 4, 0, 0],[2, 4, 6, 0],[8, 5, 9, 3]]
def maximum_path_sumI(tri):
    rows = len(tri)
    for r in range(rows-2,-1,-1):
        for c in range(r+1):
            tri[r][c] += max(tri[r+1][c], tri[r+1][c+1])
    return tri[0][0]

print(maximum_path_sumI(triangle))


