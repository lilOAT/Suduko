from solving_techniques import *
from grid_utils import *
from grid_operations import *

#========== MAIN ==========
def main():
    #Initialise grids
    grid = import_grid('Grids/Grid_nakedpairblock.csv')
    candidate_grid = create_candidate_grid()
    initialise_candidate_grid(grid, candidate_grid)

    #Print grids
    print()
    print("Starting grid:")
    print_grid(grid)
    print()
    print("Candidate grid:")
    print_candidate_grid(candidate_grid)

    #COMPUTE SOLUTION
    solve_grid(candidate_grid,grid)
    
    print()
    print("Final grid:")
    print_grid(grid)
    print()
    print("Final candidate grid:")
    print_candidate_grid(candidate_grid)

    if not is_grid_complete(grid):
        print()
        new_candidate_grid = create_candidate_grid()
        initialise_candidate_grid(grid, new_candidate_grid)
        print("Does final candidate grid match calculated grid:")
        print(candidate_grid == new_candidate_grid)
 
    #Save final grid state
    print()
    print("Saving current grid as CSV")
    export_grid(grid)
    print()

    #Test
    print()
    print("test...")

"""
    test_grid = import_grid("Grids/Grid_hiddenpaircol.csv")
    test_candidate_grid = create_candidate_grid()
    initialise_candidate_grid(test_grid, test_candidate_grid)
    print_candidate_grid(test_candidate_grid)
"""

if __name__ == '__main__':
    main()