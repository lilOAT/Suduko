def solve_cell(candidate_grid, grid, i, j, cell_solution):
    grid[i][j] = cell_solution
    print(f"-- CELL {i,j} SOLVED WITH {cell_solution}")
    #Clear solved cell's candidate cell
    for x in range(9):
        candidate_grid[i][j][x] = "."
    update_candidate_grid(candidate_grid, i, j, cell_solution)

def is_grid_complete(grid):
#Returns true if grid is complete
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    return True


def update_candidate_grid(candidate_grid, i, j, cell_solution):
    update_candidate_row(candidate_grid, i, cell_solution)
    update_candidate_col(candidate_grid, j, cell_solution)
    update_candidate_block(candidate_grid, i, j, cell_solution)

def update_candidate_row(candidate_grid, i, cell_solution):
    for j in range(9):
        if cell_solution in candidate_grid[i][j]:
            candidate_grid[i][j][cell_solution-1] = "."

def update_candidate_col(candidate_grid, j, cell_solution):
    for i in range(9):
        if cell_solution in candidate_grid[i][j]:
            candidate_grid[i][j][cell_solution-1] = "."

def update_candidate_block(candidate_grid, i, j, cell_solution):
    #Set i to row start of block
    if i <= 2:
        ii = 0
    elif 3 <= i <= 5:
        ii = 3
    elif 6 <= i <= 8:
        ii = 6
    #Set j to col start of block
    if j <= 2:
        jj = 0
    elif 3 <= j <= 5:
        jj = 3
    elif 6 <= j <= 8:
        jj = 6
    
    for row_counter in range (3):
        for col_counter in range(3):
            if cell_solution in candidate_grid[ii][jj]:
                candidate_grid[ii][jj][cell_solution-1] = "."
            jj+=1
        jj-=3
        ii+=1