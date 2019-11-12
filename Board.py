class Board:
    """
      *****************CUSTOM DOCUMENTATION for Board ********************************
    Board class stores the state of the Chess board along with all the pieces.        *

      (*) comprised of an 8x8 2D Board such that i = rows and j = columns             *

            (0) the row represents the rank, (i.e rank1= 0, rank2 = 1, ... rank8 = 7) *
            (1) the columns are the files, (i.e: a=0, b=1, c=2, ........, h=7)
            (e.g): the pos of the white king ^e1 is f[0,4] while black king  ^e8 is f[7,4] *
             (e.g2): pos of ^d4 is f[3,3] while ^e5 is f[4,4] & ^f7 is f[6,5]

      (*) At the beginning of each game, the board is initialised and default positions
             for all pieces are set.
    """
    pos = i, j = [[], []]
    min_bound = 0
    max_bound = 8

    def __init__(self):
        pass
    pass
