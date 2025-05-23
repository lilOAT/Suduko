import csv

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

def print_candidate_grid(candidate_grid):          
#Prints large Candidate grid 27x27
#Function iterates through each row, printing 3 candidates at a time for each cell
#Therefor each row prints 3 lines before moving to next row
    for i in range(9):
        for j in range(9):
        #Prints values 1-3 in each candidate cell
            for k in range(3):
                val = candidate_grid[i][j][k]
                print(val if val != 0 else ".", end=" ")
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
                val = candidate_grid[i][j][k]
                print(val if val != 0 else ".", end=" ")
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
                val = candidate_grid[i][j][k]
                print(val if val != 0 else ".", end=" ")
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


def import_grid(file_name):
# Takes a CSV file and creates a 9x9 grid in the form of a 2d list
    grid = []
    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            grid.append([int(num) for num in row])
    return grid

def export_grid(grid, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(grid)
    pass


def create_candidate_grid():
# Creates a 9x9 grid with each cell containing a list of 9 candidates
    candidate_grid = []
    for i in range(9):
        candidate_grid.append([])
        for j in range(9):
            candidate_grid[i].append([])
            for k in range(9):
                candidate_grid[i][j].append(0)
    return candidate_grid

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
