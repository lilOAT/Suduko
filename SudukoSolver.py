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


def import_grid():
# Takes a CSV file and creates a 9x9 grid in the form of a 2d list
    grid = []
    with open('Grid_100.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            grid.append([int(num) for num in row])
    return grid


def create_candidate_grid():
# Creates a 9x9 grid with each cell containing a 3x3 grid                           #TODO This doesn't need to be a 3x3 grid, 1D list will work
    candidate_grid = []                                                             #   3x3 grid will be virtualised in the print_candidate_grid method
    for i in range(9):
        candidate_grid.append([])
        for j in range(9):
            candidate_grid[i].append([])
            #candidate_grid[i].append(j)
            for k in range(3):
                candidate_grid[i][j].append([])
                for l in range(3):
                    candidate_grid[i][j][k].append(0)

    return candidate_grid


def populate_candidate_grid(candidate_grid):
# populates candidate grid with coordinates for debugging
    for i in range(9):
        for j in range(9):
            for k in range(3):
                for l in range(3):
                    candidate_grid[i][j][k][l] = str(i)+str(j)+str(k)+str(l)


def print_candidate_grid(candidate_grid):                                           #TODO The passed in candidate_grid will not contain inner 3x3 grid.
    count = 0       # Tracks the printed row for line printing                      #   Candidates will be stored in each cell as a list. Print will still display 3x3 grid
    for i in range(9):
        for k in range(3):
            for j in range(9):
                for l in range(3):
                    val = candidate_grid[i][j][k][l]
                    print(val if val != 0 else ".", end=" ")
                
                # vertical lines
                if j != 8:
                    if j % 3 == 2 and j != 0:
                        print("|| ",end="")
                    else:
                        print("| ",end="")

            print()     # new line after each row
            count+=1

            # horizontal lines
            if count % 3 == 0 and count != 27:
                if count % 9 == 0:
                    print("=" * 71)     # print = for every 9th line
                else:
                    print("-" * 71)     # print - for every 3rd line



#========== MAIN ==========
def main():
    grid = import_grid()
    print_grid(grid)
    print(f"[3][0] = {grid[3][0]}")
    print(f"[3][3] = {grid[3][3]}")

    print()

    # Testing possible_grid structure
    candidate_grid = create_candidate_grid()
    #populate_candidate_grid(candidate_grid)
    print_candidate_grid(candidate_grid)

if __name__ == '__main__':
    main()