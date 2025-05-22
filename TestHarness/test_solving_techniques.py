import sys
import copy
sys.path.append("/Users/joelpita/Documents/Coding/Python Practise/Suduko")
from solving_techniques import *
from grid_utils import *

def test_naked_single_check():
    result = "Pass"
    original_grid = [
        [0,0,5,0,0,3,0,0,0],
        [0,7,4,0,0,0,3,8,0],
        [0,8,0,0,0,4,0,5,2],
        [9,0,2,4,0,5,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,9,0,1,5,0,7],
        [8,3,0,1,0,0,0,2,0],
        [0,4,6,0,0,0,7,3,0],
        [0,0,0,5,0,0,4,0,0]
    ]
    original_candidate_grid = [
        [
            #Row 0
            [1,2,0,0,0,6,0,0,0],
            [1,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,4,0,6,7,0,9],
            [1,0,0,4,0,6,0,0,9]
        ],
        [
            #Row 1
            [1,2,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,0,0,0],
            [1,2,0,0,5,6,0,0,9],
            [0,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9]
        ],
        [
            #Row 2
            [1,0,3,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,3,0,0,0,0,0,9],
            [0,0,0,0,0,6,7,0,0],
            [1,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 3
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,6,7,8,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,8,0],
            [1,0,0,0,0,6,0,0,0],
            [1,0,3,0,0,6,0,8,0]
        ],
        [
            #Row 4
            [1,0,3,4,5,6,7,0,0],
            [1,0,0,0,5,6,0,0,0],
            [1,0,3,0,0,0,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,0,8,9],
            [1,0,0,4,0,6,0,0,9],
            [1,0,3,4,0,6,0,8,9]
        ],
        [
            #Row 5
            [0,0,3,4,0,6,0,0,0],
            [0,0,0,0,0,6,0,0,0],
            [0,0,3,0,0,0,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 6
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,7,0,9],
            [0,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,5,6,0,0,9]
        ],
        [
            #Row 7
            [1,2,0,0,5,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,8,0],
            [0,2,0,0,0,0,0,8,9],
            [0,2,0,0,0,0,0,8,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,5,0,0,8,9]
        ],
        [
            #Row 8
            [1,2,0,0,0,0,7,0,0],
            [1,2,0,0,0,0,0,0,9],
            [1,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,7,8,9],
            [0,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,0,0,6,0,8,9]
        ]
    ]

    tested_grid = copy.deepcopy(original_grid)
    tested_candidate_grid = copy.deepcopy(original_candidate_grid)
    expected_grid = copy.deepcopy(original_grid)
    expected_candidate_grid = copy.deepcopy(original_candidate_grid)

    #Test on grid with no naked singles
    #Edit candidate grid so there are no naked singles
    tested_candidate_grid[5][1][0] = 1
    expected_candidate_grid[5][1][0] = 1
    naked_single_check(tested_candidate_grid, tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail"

    #Test on grid with naked single in candidate grid 5,1
    #Edit candidate grid to contain a singular naked single solve
    tested_grid = copy.deepcopy(original_grid)
    tested_candidate_grid = copy.deepcopy(original_candidate_grid)
    expected_grid = copy.deepcopy(original_grid)
    expected_candidate_grid = copy.deepcopy(original_candidate_grid)
    tested_candidate_grid[3][1][1] = 2
    tested_candidate_grid[5][7][1] = 2
    expected_candidate_grid[3][1][1] = 2
    expected_candidate_grid[5][7][1] = 2
    expected_candidate_grid[5][1][5] = 0
    expected_candidate_grid[3][1][5] = 0
    expected_candidate_grid[5][7][5] = 0
    expected_candidate_grid[4][0][5] = 0
    expected_candidate_grid[4][1][5] = 0
    expected_candidate_grid[5][0][5] = 0
    expected_candidate_grid[5][4][5] = 0
    expected_candidate_grid[0][1][5] = 0
    expected_grid[5][1] = 6
    naked_single_check(tested_candidate_grid, tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail"

    return result

def test_hidden_single_row_check():
    result = "Pass"
    original_grid = [
        [0,0,5,0,0,3,0,0,0],
        [0,7,4,0,0,0,3,8,0],
        [0,8,0,0,0,4,0,5,2],
        [9,0,2,4,0,5,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,9,0,1,5,0,7],
        [8,3,0,1,0,0,0,2,0],
        [0,4,6,0,0,0,7,3,0],
        [0,0,0,5,0,0,4,0,0]
    ]
    original_candidate_grid = [
        [
            #Row 0
            [1,2,0,0,0,6,0,0,0],
            [1,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,4,0,6,7,0,9],
            [1,0,0,4,0,6,0,0,9]
        ],
        [
            #Row 1
            [1,2,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,0,0,0],
            [1,2,0,0,5,6,0,0,9],
            [0,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9]
        ],
        [
            #Row 2
            [1,0,3,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,3,0,0,0,0,0,9],
            [0,0,0,0,0,6,7,0,0],
            [1,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 3
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,6,7,8,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,8,0],
            [1,0,0,0,0,6,0,0,0],
            [1,0,3,0,0,6,0,8,0]
        ],
        [
            #Row 4
            [1,0,3,4,5,6,7,0,0],
            [1,0,0,0,5,6,0,0,0],
            [1,0,3,0,0,0,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,0,8,9],
            [1,0,0,4,0,6,0,0,9],
            [1,0,3,4,0,6,0,8,9]
        ],
        [
            #Row 5
            [0,0,3,4,0,6,0,0,0],
            [0,0,0,0,0,6,0,0,0],
            [0,0,3,0,0,0,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 6
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,7,0,9],
            [0,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,5,6,0,0,9]
        ],
        [
            #Row 7
            [1,2,0,0,5,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,8,0],
            [0,2,0,0,0,0,0,8,9],
            [0,2,0,0,0,0,0,8,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,5,0,0,8,9]
        ],
        [
            #Row 8
            [1,2,0,0,0,0,7,0,0],
            [1,2,0,0,0,0,0,0,9],
            [1,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,7,8,9],
            [0,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,0,0,6,0,8,9]
        ]
    ]

    tested_grid = copy.deepcopy(original_grid)
    tested_candidate_grid = copy.deepcopy(original_candidate_grid)
    expected_grid = copy.deepcopy(original_grid)
    expected_candidate_grid = copy.deepcopy(original_candidate_grid)

    #Test on grid with no hidden singles
    tested_candidate_grid[1][3][4] = 5
    tested_candidate_grid[3][1][6] = 7
    tested_candidate_grid[5][2][1] = 2
    tested_candidate_grid[6][2][3] = 4
    tested_candidate_grid[6][2][4] = 5
    tested_candidate_grid[8][2][2] = 3
    expected_candidate_grid[1][3][4] = 5
    expected_candidate_grid[3][1][6] = 7
    expected_candidate_grid[5][2][1] = 2
    expected_candidate_grid[6][2][3] = 4
    expected_candidate_grid[6][2][4] = 5
    expected_candidate_grid[8][2][2] = 3
    hidden_single_row_check(tested_candidate_grid,tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail"

    #Test on grid with first hidden single 2 in row 5. Function exits after finding first encounter
    #create hidden single
    tested_candidate_grid[5][2][1] = 0
    expected_candidate_grid[5][2][1] = 0
    #cover naked single (to stop recursion in naked_single_check)
    tested_candidate_grid[5][1][3] = 4
    expected_candidate_grid[5][1][3] = 4
    #expected results
    expected_candidate_grid[5][4] = [0,0,0,0,0,0,0,0,0]
    expected_grid[5][4] = 2
    expected_candidate_grid[0][4][1] = 0
    expected_candidate_grid[1][4][1] = 0
    expected_candidate_grid[4][4][1] = 0
    expected_candidate_grid[7][4][1] = 0
    expected_candidate_grid[8][4][1] = 0
    expected_candidate_grid[4][3][1] = 0
    expected_candidate_grid[4][5][1] = 0

    hidden_single_row_check(tested_candidate_grid, tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail"

    return result

def test_hidden_single_col_check():
    result = "Pass"
    original_grid = [
        [0,0,5,0,0,3,0,0,0],
        [0,7,4,0,0,0,3,8,0],
        [0,8,0,0,0,4,0,5,2],
        [9,0,2,4,0,5,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,9,0,1,5,0,7],
        [8,3,0,1,0,0,0,2,0],
        [0,4,6,0,0,0,7,3,0],
        [0,0,0,5,0,0,4,0,0]
    ]
    original_candidate_grid = [
        [
            #Row 0
            [1,2,0,0,0,6,0,0,0],
            [1,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,4,0,6,7,0,9],
            [1,0,0,4,0,6,0,0,9]
        ],
        [
            #Row 1
            [1,2,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,0,0,0],
            [1,2,0,0,5,6,0,0,9],
            [0,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9]
        ],
        [
            #Row 2
            [1,0,3,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,3,0,0,0,0,0,9],
            [0,0,0,0,0,6,7,0,0],
            [1,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 3
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,6,7,8,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,8,0],
            [1,0,0,0,0,6,0,0,0],
            [1,0,3,0,0,6,0,8,0]
        ],
        [
            #Row 4
            [1,0,3,4,5,6,7,0,0],
            [1,0,0,0,5,6,0,0,0],
            [1,0,3,0,0,0,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,0,8,9],
            [1,0,0,4,0,6,0,0,9],
            [1,0,3,4,0,6,0,8,9]
        ],
        [
            #Row 5
            [0,0,3,4,0,6,0,0,0],
            [0,0,0,0,0,6,0,0,0],
            [0,0,3,0,0,0,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 6
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,7,0,9],
            [0,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,5,6,0,0,9]
        ],
        [
            #Row 7
            [1,2,0,0,5,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,8,0],
            [0,2,0,0,0,0,0,8,9],
            [0,2,0,0,0,0,0,8,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,5,0,0,8,9]
        ],
        [
            #Row 8
            [1,2,0,0,0,0,7,0,0],
            [1,2,0,0,0,0,0,0,9],
            [1,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,7,8,9],
            [0,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,0,0,6,0,8,9]
        ]
    ]

    tested_grid = copy.deepcopy(original_grid)
    tested_candidate_grid = copy.deepcopy(original_candidate_grid)
    expected_grid = copy.deepcopy(original_grid)
    expected_candidate_grid = copy.deepcopy(original_candidate_grid)

    #Test on grid with no hidden singles
    tested_candidate_grid[3][1][4] = 5
    tested_candidate_grid[2][3][2] = 3
    tested_candidate_grid[0][4][3] = 4
    tested_candidate_grid[0][4][4] = 5
    tested_candidate_grid[3][6][1] = 2
    tested_candidate_grid[3][7][6] = 7
    expected_candidate_grid[3][1][4] = 5
    expected_candidate_grid[2][3][2] = 3
    expected_candidate_grid[0][4][3] = 4
    expected_candidate_grid[0][4][4] = 5
    expected_candidate_grid[3][6][1] = 2
    expected_candidate_grid[3][7][6] = 7

    hidden_single_col_check(tested_candidate_grid,tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail at no hidden singles"

    #Test on grid with first hidden single 2 in col 6. Function exits after finding first encounter
    #create hidden single
    tested_candidate_grid[3][6][1] = 0
    expected_candidate_grid[3][6][1] = 0
    #cover naked single (to stop recursion in naked_single_check)
    tested_candidate_grid[5][1][0] = 1
    expected_candidate_grid[5][1][0] = 1
    #expected results
    expected_candidate_grid[4][6] = [0,0,0,0,0,0,0,0,0]
    expected_grid[4][6] = 2
    expected_candidate_grid[4][3][1] = 0
    expected_candidate_grid[4][4][1] = 0
    expected_candidate_grid[4][5][1] = 0

    hidden_single_col_check(tested_candidate_grid, tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail"

    return result

def test_hidden_single_block_check():
    result = "Pass"
    original_grid = [
        [0,0,5,0,0,3,0,0,0],
        [0,7,4,0,0,0,3,8,0],
        [0,8,0,0,0,4,0,5,2],
        [9,0,2,4,0,5,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,9,0,1,5,0,7],
        [8,3,0,1,0,0,0,2,0],
        [0,4,6,0,0,0,7,3,0],
        [0,0,0,5,0,0,4,0,0]
    ]
    original_candidate_grid = [
        [
            #Row 0
            [1,2,0,0,0,6,0,0,0],
            [1,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,4,0,6,7,0,9],
            [1,0,0,4,0,6,0,0,9]
        ],
        [
            #Row 1
            [1,2,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,6,0,0,0],
            [1,2,0,0,5,6,0,0,9],
            [0,2,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9]
        ],
        [
            #Row 2
            [1,0,3,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,3,0,0,0,0,0,9],
            [0,0,0,0,0,6,7,0,0],
            [1,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 3
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,3,0,0,6,7,8,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,8,0],
            [1,0,0,0,0,6,0,0,0],
            [1,0,3,0,0,6,0,8,0]
        ],
        [
            #Row 4
            [1,0,3,4,5,6,7,0,0],
            [1,0,0,0,5,6,0,0,0],
            [1,0,3,0,0,0,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,3,0,0,6,7,8,0],
            [0,2,0,0,0,6,7,8,0],
            [1,2,0,0,0,6,0,8,9],
            [1,0,0,4,0,6,0,0,9],
            [1,0,3,4,0,6,0,8,9]
        ],
        [
            #Row 5
            [0,0,3,4,0,6,0,0,0],
            [0,0,0,0,0,6,0,0,0],
            [0,0,3,0,0,0,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,0,8,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,0,0,0],
            [0,0,0,0,0,0,0,0,0]
        ],
        [
            #Row 6
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,4,0,6,7,0,9],
            [0,0,0,0,0,6,7,0,9],
            [0,0,0,0,0,6,0,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,5,6,0,0,9]
        ],
        [
            #Row 7
            [1,2,0,0,5,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [0,2,0,0,0,0,0,8,0],
            [0,2,0,0,0,0,0,8,9],
            [0,2,0,0,0,0,0,8,9],
            [0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,5,0,0,8,9]
        ],
        [
            #Row 8
            [1,2,0,0,0,0,7,0,0],
            [1,2,0,0,0,0,0,0,9],
            [1,0,0,0,0,0,7,0,9],
            [0,0,0,0,0,0,0,0,0],
            [0,2,3,0,0,6,7,8,9],
            [0,2,0,0,0,6,7,8,9],
            [0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,6,0,0,9],
            [1,0,0,0,0,6,0,8,9]
        ]
    ]

    tested_grid = copy.deepcopy(original_grid)
    tested_candidate_grid = copy.deepcopy(original_candidate_grid)
    expected_grid = copy.deepcopy(original_grid)
    expected_candidate_grid = copy.deepcopy(original_candidate_grid)

    #Test on grid with no hidden singles
    tested_candidate_grid[8][0][4] = 5
    tested_candidate_grid[0][3][4] = 5
    tested_candidate_grid[8][5][2] = 3
    tested_candidate_grid[8][5][3] = 4
    tested_candidate_grid[0][6][6] = 7
    tested_candidate_grid[3][6][1] = 2
    expected_candidate_grid[8][0][4] = 5
    expected_candidate_grid[0][3][4] = 5
    expected_candidate_grid[8][5][2] = 3
    expected_candidate_grid[8][5][3] = 4
    expected_candidate_grid[0][6][6] = 7
    expected_candidate_grid[3][6][1] = 2

    hidden_single_block_check(tested_candidate_grid,tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail at no hidden singles"

    #Test on grid with first hidden single 5 in block 7. Function exits after finding first encounter
    #Reset grids
    tested_grid = copy.deepcopy(original_grid)
    tested_candidate_grid = copy.deepcopy(original_candidate_grid)
    expected_grid = copy.deepcopy(original_grid)
    expected_candidate_grid = copy.deepcopy(original_candidate_grid)
    #cover naked single (to stop recursion in naked_single_check)
    tested_candidate_grid[5][1][0] = 1
    expected_candidate_grid[5][1][0] = 1
    #expected results
    expected_candidate_grid[7][0] = [0,0,0,0,0,0,0,0,0]
    expected_grid[7][0] = 5
    expected_candidate_grid[4][0][4] = 0
    expected_candidate_grid[7][8][4] = 0

    hidden_single_block_check(tested_candidate_grid, tested_grid)
    if not (tested_grid == expected_grid and tested_candidate_grid == expected_candidate_grid):
        result = "Fail"

    return result

def test_naked_pair_row_check():
    result = "Pass"
    pass