import csv

#========== FUNCTIONS ==========
def print_grid(grid):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # horizontal divider every 3 rows
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # vertical divider every 3 columns
            val = grid[i][j]
            print(val if val != 0 else ".", end=" ")
        print()  # new line after each row
    print()

def import_grid(file_name):
# Takes a CSV file and creates a 9x9 grid in the form of a 2d list
    grid = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            grid.append([int(num) for num in row])
    return grid


def create_candidate_grid():
# Creates a 9x9 grid with each cell containing a list of 9 candidates
    candidate_grid = []
    for i in range(9):
        candidate_grid.append([])
        for j in range(9):
            candidate_grid[i].append([])
            for k in range(9):
                candidate_grid[i][j].append(".")
    return candidate_grid

def populate_candidate_grid(candidate_grid):
#DEPRECATED
# populates candidate grid with values for debugging
    for i in range(9):
        for j in range(9):
            for k in range(9):
                    candidate_grid[i][j][k] = str(i)+str(j)+str(k)

def print_candidate_grid(candidate_grid):          
#Prints large Candidate grid 27x27
#Function iterates through each row, printing 3 candidates at a time for each cell
#Therefor each row prints 3 lines before moving to next row
    for i in range(9):
        for j in range(9):
        #Prints values 1-3 in each candidate cell
            for k in range(3):
                print(candidate_grid[i][j][k], end=" ")
            #Printing lines
            if j % 3 == 2 and j != 8:
                print("||", end=" ")
            elif j != 8:
                print("|", end=" ")
            else:
                print()
        for j in range(9):
        #Prints values 4-6 in each candidate cell
            for k in range(3, 6):
                print(candidate_grid[i][j][k], end=" ")
            #Printing lines
            if j % 3 == 2 and j != 8:
                print("||", end=" ")
            elif j != 8:
                print("|", end=" ")
            else:
                print()
        for j in range(9):
        #Prints values 7-9 in each candidate cell
            for k in range(6, 9):
                print(candidate_grid[i][j][k], end=" ")
            #Printing lines
            if j % 3 == 2 and j != 8:
                print("||", end=" ")
            elif j != 8:
                print("|", end=" ")
            else:
                print()
        
        #Horizontal lines
        if i % 3 != 2:
            print("-" * 71)
        elif i != 8:
            print("=" * 71)

def initialise_candidate_grid(grid, candidate_grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:
                for x in range(1,10):
                    if not is_number_in_block(x, i, j, grid):
                        if not is_number_in_row(x, i, grid):
                            if not is_number_in_col(x, j, grid):
                                candidate_grid[i][j][x-1] = x


def is_number_in_block(x, i, j, grid):
    block_contains_x = False
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
            if x == grid[ii][jj]:
                block_contains_x = True
                #DEBUG print(f"Set true @{ii,jj} for x{x}")
            jj+=1
        jj-=3
        ii+=1
    return block_contains_x

def is_number_in_row(x, i, grid):
    row_contains_x = False
    for jj in range(9):
        if x == grid[i][jj]:
            row_contains_x = True
    return row_contains_x

def is_number_in_col(x, j, grid):
    col_contains_x = False
    for ii in range(9):
        if x == grid[ii][j]:
            col_contains_x = True
    return col_contains_x


def solve_cell(candidate_grid, grid, i, j, cell_solution):
    grid[i][j] = cell_solution
    #Clear solved cell's candidate cell
    for x in range(9):
        candidate_grid[i][j][x] = "."
    update_candidate_grid(candidate_grid, i, j, cell_solution)

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


def grid_scan(candidate_grid, grid):
#This wrapper function only runs its functions if the grid isn't solved.
#The idea is to reduce the redundant recursion collapse after complete solve.
    #Naked Single Check
    if not is_grid_complete(grid):
        print()
        print("Executing: Naked Single Check...")
        naked_single_check(candidate_grid, grid)
    #Hidden Single Check
    if not is_grid_complete(grid):
        print()
        print("Executing: Hidden Single Check...")
        hidden_single_check(candidate_grid, grid)
    #Naked Pair Check
    if not is_grid_complete(grid):
        print()
        print("Executing: Naked Pair Check")
        naked_pair_check(candidate_grid, grid)

def is_grid_complete(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                return False
    return True


def naked_single_check(candidate_grid, grid):
    for i in range(9):
        for j in range(9):
            non_candidate_count = candidate_grid[i][j].count(".")
            if non_candidate_count == 8:
                cell_solution = next(item for item in candidate_grid[i][j] if isinstance(item, int))
                print(cell_solution, "at ", i,j)
                solve_cell(candidate_grid, grid, i, j, cell_solution)
                naked_single_check(candidate_grid, grid)
                return


def hidden_single_check(candidate_grid, grid):
    hidden_single_row_check(candidate_grid, grid)
    hidden_single_col_check(candidate_grid, grid)
    hidden_single_block_check(candidate_grid, grid)

def hidden_single_row_check(candidate_grid, grid):
    for curr_candidate in range(1,10):
        for i in range(9):
            candidate_count = 0
            for j in range(9):
                if curr_candidate in candidate_grid[i][j]:
                    candidate_count += 1
                    ii = i
                    jj = j
            if candidate_count == 1:
                print(f"hidden single row found ({curr_candidate}) at {ii,jj}")
                solve_cell(candidate_grid, grid, ii, jj, curr_candidate)
                naked_single_check(candidate_grid, grid)
                hidden_single_check(candidate_grid, grid)
                return

def hidden_single_col_check(candidate_grid, grid):
    for curr_candidate in range(1,10):
        for j in range(9):
            candidate_count = 0
            for i in range(9):
                if curr_candidate in candidate_grid[i][j]:
                    candidate_count += 1
                    ii = i
                    jj = j
            if candidate_count == 1:
                print(f"hidden single col found ({curr_candidate}) at {ii,jj}")
                solve_cell(candidate_grid, grid, ii, jj, curr_candidate)
                naked_single_check(candidate_grid, grid)
                hidden_single_check(candidate_grid, grid)
                return

def hidden_single_block_check(candidate_grid, grid):
    i = 0
    j = 0
    for block in range(9):
        for curr_candidate in range(1,10):
            candidate_count = 0
            #Search block
            #print(f"Checking block @{i,j}")
            for row_count in range(3):
                for col_count in range(3):
                    if curr_candidate in candidate_grid[i][j]:
                        candidate_count += 1
                        ii = i
                        jj = j
                    j+=1
                j-=3
                i+=1
            i -= 3
            #print("Candidate ", curr_candidate, " occurs ", candidate_count)
            if candidate_count == 1:
                print(f"hidden single block found ({curr_candidate}) at {ii,jj}")
                solve_cell(candidate_grid, grid, ii, jj, curr_candidate)
                naked_single_check(candidate_grid, grid)
                hidden_single_check(candidate_grid, grid)
                return
        #Move to next block
        if i != 6:
            i += 3
        else:
            i = 0
            j += 3


def naked_pair_check(candidate_grid, grid):
    naked_pair_row_check(candidate_grid, grid)
    #naked_pair_col_check(candidate_grid, grid)
    #naked_pair_block_check(candidate_grid, grid)

def naked_pair_row_check(candidate_grid, grid):
    for i in range(9):
        for j in range(9):
            candidate_count = 9 - candidate_grid[i][j].count(".")
            if candidate_count == 2:
                #Save 2 candidates
                naked_pair_1 = []
                for item in candidate_grid[i][j]:
                    if isinstance(item, int):
                        naked_pair_1.append(item)

                #Check through remaining cells in row
                for jj in range(j+1,9):
                    candidate_count = 9 - candidate_grid[i][jj].count(".")
                    if candidate_count == 2:
                        #Save 2 candidates
                        naked_pair_2 = []
                        for item_in_next in candidate_grid[i][jj]:
                            if isinstance(item_in_next, int):
                                naked_pair_2.append(item_in_next)
                        #if contains same candidates, remove all other occurances of candidates
                        if naked_pair_1 == naked_pair_2:
                            for jjj in range(9):
                                #Don't remove the naked pair cells
                                if jjj != jj and jjj != j:
                                    for naked_pair_item in naked_pair_1:
                                        if naked_pair_item in candidate_grid[i][jjj]:
                                            candidate_grid[i][jjj][naked_pair_item-1] = "."
                                            naked_single_check(candidate_grid, grid)
                                            hidden_single_check(candidate_grid, grid)

def naked_pair_col_check(candidate_grid, grid):
    pass

def naked_pair_block_check(candidate_grid, grid):
    pass
                
                    

#========== MAIN ==========
def main():
    #Initialise grids
    grid = import_grid('Grid_hidden+nakedpair.csv')
    candidate_grid = create_candidate_grid()
    initialise_candidate_grid(grid, candidate_grid)

    #Print grids
    print()
    print("Starting grid:")
    print_grid(grid)
    print()
    print("Candidate grid:")
    print_candidate_grid(candidate_grid)

    
    print()
    print("Final grid:")
    print_grid(grid)
    print()
    print("Final candidate grid:")
    print_candidate_grid(candidate_grid)

    print()
    print("test...")
    print(is_grid_complete(grid))


if __name__ == '__main__':
    main()