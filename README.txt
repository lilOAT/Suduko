
Definitions
    Cell
    Block
    Row
    Collumn
    House           Either Block, Row or Collumn


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

[row][col][inner row][inner col]
    Identify the larger, outside Block first, then inner coordinates
    The '0' coordinates are [0][1][0][1]
. . . | . . . | . . . || . 0 . | . . . | . . . || . . . | . . . | . . . 
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


-----------
SUDO

hidden_single_check()
    CHECK HIDDEN SINGLE ROW
    CHECK HIDDEN SINGLE COLLUMN
    CHECK HIDDEN SINGLE BLOCK

naked_single_check()
    CHECK NAKED SINGLE ROW
    CHECK NAKED SINGLE COLLUMN
    CHECK NAKED SINGLE BLOCK

hidden_pair_check()
    CHECK HIDDEN PAIR ROW
    CHECK HIDDEN PAIR COLLUMN
    CHECK HIDDEN PAIR BLOCK

naked_pair_check()
    CHECK NAKED PAIR ROW
    CHECK NAKED PAIR COLLUMN
    CHECK NAKED PAIR BLOCK