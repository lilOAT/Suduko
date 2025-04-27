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
# populates candidate grid with values for debugging
    for i in range(9):
        for j in range(9):
            for k in range(3):
                for l in range(3):
                    candidate_grid[i][j][k][l] = str(i)+str(j)+str(k)+str(l)


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


#========== MAIN ==========
def main():
    grid = import_grid()
    print_grid(grid)
    print(f"[3][0] = {grid[3][0]}")
    print(f"[3][3] = {grid[3][3]}")

    print()

    # Testing possible_grid structure
    candidate_grid = create_candidate_grid()
    print_candidate_grid(candidate_grid)


if __name__ == '__main__':
    main()