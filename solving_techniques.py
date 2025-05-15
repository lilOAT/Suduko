from grid_operations import *

def solve_grid(candidate_grid, grid):
    is_complete = False
    for run_times in range(10):
        naked_single_check(candidate_grid, grid)
        hidden_single_check(candidate_grid, grid)
        naked_pair_check(candidate_grid, grid)
        is_complete = is_grid_complete(grid)
        if is_complete:
            print()
            print("SOLVED")
            print(f"Number of full loops required: {run_times}")
            return
        print("------------- END LOOP -------------")


def naked_single_check(candidate_grid, grid):
#If there is a naked single: sovle cell -> recurse function -> end
    if __debug__:
        print("Entering naked single")
    for i in range(9):
        for j in range(9):
            non_candidate_count = candidate_grid[i][j].count(0)
            if non_candidate_count == 8:
                cell_solution = next(item for item in candidate_grid[i][j] if item != 0)
                if __debug__:
                    print(f"  naked single found {cell_solution} at {i,j}")
                solve_cell(candidate_grid, grid, i, j, cell_solution)
                naked_single_check(candidate_grid, grid)
                return


def hidden_single_check(candidate_grid, grid):
        hidden_single_row_check(candidate_grid, grid)
        hidden_single_col_check(candidate_grid, grid)
        hidden_single_block_check(candidate_grid, grid)

def hidden_single_row_check(candidate_grid, grid):
    if __debug__:
        print("Entering hidden single row check")
    for curr_candidate in range(1,10):
        for i in range(9):
            candidate_count = 0
            for j in range(9):
                if curr_candidate in candidate_grid[i][j]:
                    candidate_count += 1
                    ii = i
                    jj = j
            if candidate_count == 1:
                if __debug__:
                    print(f"  hidden single row found {curr_candidate} at {ii,jj}")
                solve_cell(candidate_grid, grid, ii, jj, curr_candidate)
                naked_single_check(candidate_grid, grid)
                #hidden_single_check(candidate_grid, grid)
                return

def hidden_single_col_check(candidate_grid, grid):
    if __debug__:
        print("Entering hidden single col check")
    for curr_candidate in range(1,10):
        for j in range(9):
            candidate_count = 0
            for i in range(9):
                if curr_candidate in candidate_grid[i][j]:
                    candidate_count += 1
                    ii = i
                    jj = j
            if candidate_count == 1:
                if __debug__:
                    print(f"hidden single col found {curr_candidate} at {ii,jj}")
                solve_cell(candidate_grid, grid, ii, jj, curr_candidate)
                naked_single_check(candidate_grid, grid)
                #hidden_single_check(candidate_grid, grid)
                return

def hidden_single_block_check(candidate_grid, grid):
    if __debug__:
        print("Entering hidden single block check")
    i = 0
    j = 0
    for block in range(9):
        for curr_candidate in range(1,10):
            candidate_count = 0
            #Search block
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
                if __debug__:
                    print(f"  hidden single block found {curr_candidate} at {ii,jj}")
                solve_cell(candidate_grid, grid, ii, jj, curr_candidate)
                naked_single_check(candidate_grid, grid)
                #hidden_single_check(candidate_grid, grid)
                return
        #Move to next block
        if i != 6:
            i += 3
        else:
            i = 0
            j += 3


def naked_pair_check(candidate_grid, grid):
    naked_pair_row_check(candidate_grid, grid)
    naked_pair_col_check(candidate_grid, grid)
    naked_pair_block_check(candidate_grid, grid)

def naked_pair_row_check(candidate_grid, grid):
    print("Entering naked pair row check")
    for i in range(9):
        for j in range(9):
            candidate_count = 9 - candidate_grid[i][j].count(0)
            if candidate_count == 2:
                #Save 2 candidates
                naked_pair_1 = []
                for item in candidate_grid[i][j]:
                    if item != 0:
                        naked_pair_1.append(item)

                #Check through remaining cells in row
                for jj in range(j+1,9):
                    candidate_count = 9 - candidate_grid[i][jj].count(0)
                    if candidate_count == 2:
                        #Save 2 candidates
                        naked_pair_2 = []
                        for item_in_next in candidate_grid[i][jj]:
                            if item_in_next != 0:
                                naked_pair_2.append(item_in_next)
                        #if contains same candidates, remove all other occurances of candidates
                        if naked_pair_1 == naked_pair_2:
                            print(f"  Naked pair {naked_pair_1} found at: {i,j} and {i,jj}")
                            for jjj in range(9):
                                #Don't remove the naked pair cells
                                if jjj != jj and jjj != j:
                                    for naked_pair_item in naked_pair_1:
                                        if naked_pair_item in candidate_grid[i][jjj]:
                                            candidate_grid[i][jjj][naked_pair_item-1] = 0
                                            print(f"    Removed candidate {naked_pair_item} in {i,jjj}")
                            
def naked_pair_col_check(candidate_grid, grid):
    print("Entering naked pair col check")
    for j in range(9):
        for i in range(9):
            candidate_count = 9 - candidate_grid[i][j].count(0)
            if candidate_count == 2:
                #Save 2 candidates
                naked_pair_1 = []
                for item in candidate_grid[i][j]:
                    if item != 0:
                        naked_pair_1.append(item)

                #Check through remaining cells in row
                for ii in range(i+1,9):
                    candidate_count = 9 - candidate_grid[ii][j].count(0)
                    if candidate_count == 2:
                        #Save 2 candidates
                        naked_pair_2 = []
                        for item_in_next in candidate_grid[ii][j]:
                            if item_in_next != 0:
                                naked_pair_2.append(item_in_next)
                        #if contains same candidates, remove all other occurances of candidates
                        if naked_pair_1 == naked_pair_2:
                            print(f"  Naked pair {naked_pair_1} found at: {i,j} and {ii,j}")
                            for iii in range(9):
                                #Don't remove the naked pair cells
                                if iii == ii and iii == i:
                                    for naked_pair_item in naked_pair_1:
                                        if naked_pair_item in candidate_grid[iii][j]:
                                            candidate_grid[iii][j][naked_pair_item-1] = 0
                                            print(f"    Removed candidate {naked_pair_item} in {iii,j}")
                            
def naked_pair_block_check(candidate_grid, grid):
    print("Entering naked pair block check")
    i = 0
    j = 0
    ii = 0
    jj = 0
    iii = 0
    jjj = 0
    for block in range(9):
            for row_count in range(3):
                for col_count in range(3):
                    candidate_count = 9 - candidate_grid[i][j].count(0)
                    if candidate_count == 2:
                        #Save 2 candidates
                        naked_pair_1 = []
                        for item in candidate_grid[i][j]:
                            if item != 0:
                                naked_pair_1.append(item)

                        #Check through remaining cells in the block
                        for row_count2 in range(3):
                            for col_count2 in range(3):
                                if not (ii == i and jj == j):
                                    candidate_count = 9 - candidate_grid[ii][jj].count(0)
                                    if candidate_count == 2:
                                        #Save 2 candidates
                                        naked_pair_2 = []
                                        for item in candidate_grid[ii][jj]:
                                            if item != 0:
                                                naked_pair_2.append(item)
                                        #if contains same candidates, remove all other occurances of candidates
                                        if naked_pair_1 == naked_pair_2:
                                            print(f"  Naked pair {naked_pair_1} found at: {i,j} and {ii,jj}")

                                            for row_count3 in range(3):
                                                for col_count3 in range(3):
                                                    #Don't remove the naked pair cells          #TODO v not done
                                                    if not (iii == i and jjj == j) and not (iii == ii and jjj == jj):                   #if iterated cell not one of the cells that have naked pair
                                                        for naked_pair_item in naked_pair_1:
                                                            if naked_pair_item in candidate_grid[iii][jjj]:
                                                                candidate_grid[iii][jjj][naked_pair_item-1] = 0
                                                                print(f"    Removed candidate {naked_pair_item} in {iii,jjj}")
                                                    jjj+=1
                                                jjj-=3
                                                iii+=1
                                            #Return to start cell of block
                                            iii -= 3

                                jj+=1
                            jj-=3
                            ii+=1
                        #Return to start cell of block
                        ii -= 3

                    j+=1
                j-=3
                i+=1
            #Return to start cell of block
            i -= 3

            #Move to next block
            if i != 6:
                i += 3
                ii += 3
                iii += 3
            else:
                i = 0
                j += 3
                ii = 0
                jj += 3
                iii = 0
                jjj += 3