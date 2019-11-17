class Board:
    """
      *****************CUSTOM DOCUMENTATION for Board ********************************
    Board class stores the state of the Chess board along with all the pieces.        *

      (*) comprised of an 8x8 2D Board such that i = rows and j = columns             *

            (0) the row represents the rank, (i.e rank1= 0, rank2 = 1, ... rank8 = 7) *
            (1) the columns are the files, (i.e: a=0, b=1, c=2, ........, h=7)
            (e.g): the state of the white king ^e1 is f[0,4, K, w] while black king  ^e8 is f[7,4, K, b] *
             (e.g2): pos of ^d4 is f[3,3] while ^e5 is f[4,4] & ^f7 is f[6,5]

      (*) At the beginning of each game, the board is initialised and default positions
             for all pieces are set.
    """
    pos = i, j, S = [[], []]
    min_bound = 0
    max_bound = 8  # n < max_bound

    def __init__(self):  # default positions for all the pieces.

        pass

    def is_occupied(self, square, board):  # returns bool if a piece already stays on a square
        pass

    pass
