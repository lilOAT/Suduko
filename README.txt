Sudoku Solver
Made by Joel P (lilOAT)
Current OS - macOS 15.4.1
-----------------------------
Welcome to the Sudoku Solver, a small project I am solely developing in my free time.
The purpose is to solidify my programming skils, to learn Python and to understand GitHub.
The desired program will have a GUI for user interaction.


Functionality:
    The program takes in a csv file of an unsolved sudoku grid and outputs a solved grid.
    (STC) To change the input grid, change the filname in the main function of SudokuSolver.py

Run:
    Normal operation
        ../Sudoku % python3 SudokuSolver.py

    To remove debug messages:
        ../Sudoku % python3 -O SudokuSolver.py

    Run Test Harness:
        ../Sudoku/TestHarness % python3 -O TestHarness.py

Files:
    📦Suduko
    ┣ 📂Grids
    ┃ ┣ 📜Grid_100.csv
    ┃ ┣ 📜Grid_323.csv
    ┃ ┣ 📜Grid_500.csv
    ┃ ┣ 📜Grid_624.csv
    ┃ ┣ 📜Grid_hidden+nakedpair.csv
    ┃ ┣ 📜Grid_hiddenpairblock.csv
    ┃ ┣ 📜Grid_hiddenpaircol.csv
    ┃ ┣ 📜Grid_hiddensingleblock.csv
    ┃ ┣ 📜Grid_nakedpairblock.csv
    ┃ ┣ 📜Grid_nakedpaircol.csv
    ┃ ┗ 📜csvOut.csv
    ┣ 📂TestHarness
    ┃ ┣ 📜TestHarness.py
    ┃ ┣ 📜test_grid_operations.py
    ┃ ┣ 📜test_grid_utils.py
    ┃ ┗ 📜test_solving_techniques.py
    ┣ 📜README.txt
    ┣ 📜SudukoSolver.py
    ┣ 📜grid_operations.py
    ┣ 📜grid_utils.py
    ┗ 📜solving_techniques.py


Definitions
    Cell
    Block
    Row
    Collumn
    House
        Either Block, Row or Collumn

Blocks
    1 2 3
    4 5 6
    7 8 9

Block iteration behaviour
    1->4->7->2->5->8->3->6->9

[row][col]
    The first '5' is [0][2]
. . 5 | . . 3 | . . . 
. 7 4 | . . . | 3 8 . 
. 8 . | . . 4 | . 5 2 
---------------------
9 . 2 | 4 . 5 | . . . 
. . . | . . . | . . . 
. . . | 9 . 1 | 5 . 7 
---------------------
8 3 . | 1 . . | . 2 . 
. 4 6 | . . . | 7 3 . 
. . . | 5 . . | 4 . . 

[row][col][candidate]
    Locate the grid cell first [0][1]
    Then locate numerical value position in list of candidates
    Candidate 1 = item 0. Candidate 9 = item 8.
    The '2' coordinates are [0][1][1]
. . . | . . . | . . . || . 2 . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
-----------------------------------------------------------------------
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
-----------------------------------------------------------------------
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
=======================================================================
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
-----------------------------------------------------------------------
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
-----------------------------------------------------------------------
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
=======================================================================
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
-----------------------------------------------------------------------
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
-----------------------------------------------------------------------
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 
. . . | . . . | . . . || . . . | . . . | . . . || . . . | . . . | . . . 


Techniques
    Hidden Single
        Candidate only appears once in a house
        All other candidates in cell can be removed.
    Naked Single
        Only candidate that can solve a cell
        All other appearances of the candidate within the house can be removed
    Hidden pair
        2 candidates appear exactly twice together in 2 cells within house
        All other candidates can be removed from cell
    Naked pair
        2 cells can only be solved with the same candidates, within a house.
        All other appearances of either of these candidates within the house can be removed.
    Eliminating Single
    Locked Candidate
        When a candidate only appears in a house within another house
        eg. candidate appears in block twice in the same Collumn
            all other appearances of candidate in collumn are removed


-----------
SUDO


NAKED_SINGLE_CHECK()
    IF ANY CELL CONTAINS ONLY A SINGLE CANDIDATE
        SOLVE CELL()
        NAKED_SINGLE_CHECK()

HIDDEN_SINGLE_CHECK()
    IF ANY OF THE FOLLOWING RETURN TRUE
        CHECK HIDDEN SINGLE ROW
        CHECK HIDDEN SINGLE COLLUMN
        CHECK HIDDEN SINGLE BLOCK
    DO THIS
        SOLVE_CELL()
        NAKED_SINGLE_CHECK()
        HIDDEN_SINGLE_CHECK()

HIDDEN_PAIR_CHECK()



NAKED_PAIR_CHECK()
    SEARCH EVERY CELL IN HOUSE
        IF A CELL HAS ONLY 2 CANDIDATES
            ADD TO LIST
    FOR EVERY CELL IN LIST
        SAVE 2 CANDIDATES
        SEARCH OTHER CELLS IN LIST FOR CANDIDATE MATCH
        IF MATCH
            REMOVE ALL CANDIDATES IN ALL OTHER CELLS IN HOUSE
        IF NO MATCH
            REMOVE CELL FROM LIST            

NAKED_PAIR_CHECK()
    SEARCH EVERY CELL IN HOUSE
        IF A CELL HAS ONLY 2 CANDIDATES
            SEARCH OTHER CELLS IN LIST FOR CANDIDATE MATCH
            IF MATCH
                REMOVE ALL CANDIDATES IN ALL OTHER CELLS IN HOUSE
            IF NO MATCH
                REMOVE CELL FROM LIST           

SOLVE_CELL()
    ENTER NUMBER
    UPDATE_CANDIDATE_GRID_ROW()
    UPDATE_CANDIDATE_GRID_BLOCK()
    UPDATE_CANDIDATE_GRID_COLLUMN()

UPDATE_CANDIDATE_GRID_ROW()
    SEARCH CURR LOC ROW FOR NUMBER SOLVED
    IF CANDIDATE CELL CONTAINS NUMBER
        REMOVE NUMBER
        IF CANDIDATE CELL CONTAINS 1 NUMBER
            SOLVE_CELL()

UPDATE_CANDIDATE_GRID_COLLUMN()
    SEARCH CURR LOC COLLUMN FOR NUMBER SOLVED
    IF CANDIDATE CELL CONTAINS NUMBER
        REMOVE NUMBER
        IF CANDIDATE CELL CONTAINS 1 NUMBER
            SOLVE_CELL()

UPDATE_CANDIDATE_GRID_BLOCK()
    SEARCH CURR LOC BLOCK FOR NUMBER SOLVED
    IF CANDIDATE CELL CONTAINS NUMBER
        REMOVE NUMBER
        IF CANDIDATE CELL CONTAINS 1 NUMBER
            SOLVE_CELL()

INITIATE_CANDIDATE_GRID()
    FOR EACH EMPTY CELL
        FOR NUMBERS 1 - 9
            IF NUMBER NOT IN BLOCK
                IF NUMBER NOT IN ROW
                    IF NUMBER NOT COLLUMN
                        INSERT NUMBER INTO CANDIDATE GRID CELL





MAIN
    READ CSV FILE TO BUILD GRID
    CREATE CANDIDATE GRID
    INTIALISE CANDIDATE GRID

    NAKED_SINGLE_CHECK()
    HIDDEN_SINGLE_CHECK()





TODO
------
TEST HARNESS!!!
    Before progressing with new algorithms

Hidden pair Block - Grid_hiddenpairblock
    Block 5 has hidden pair (1,9)

Hidden pair col - Grid_hiddenpaircol
    Row 0 has hidden pair (2,6)

