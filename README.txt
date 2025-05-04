
Definitions
    Cell
    Block
    Row
    Collumn
    House           Either Block, Row or Collumn

Blocks
    1 2 3
    4 5 6
    7 8 9

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
    The '2' candidate are [0][1][1]
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
Grid_nakedpairblock,csv
    Should find naked pair 7,5 in block 1




Change block behaviour
    atm it moves 1->4->7->2->5->8->9
    should be 123456789