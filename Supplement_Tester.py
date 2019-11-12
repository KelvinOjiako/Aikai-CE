
class Minion:  # My minions will act as the debugging framework
    """
                    Chess is the struggle against the error!!
    ****** The 5 Golden rules that minions abide by ***************
    (1): At any given point in this Chess Program, the state of the board and position
            of all the pieces must always be known. (Absolute Rule!!!!)
                ****(i.e [i,j] of entire army is stored and updated)*****


    (2): Only valid moves can be made, loop continues until a valid move is entered
        e.g: king can't put himself in danger & pieces can't jump, except the knight
       e.g2: Pieces can only capture pieces from opposing side, pawns only move forward

    (3): The previous 50 states of the board must be known (Necessary for 50-move rule)

    (4): Checks the values of the following methods
                i) mate (ii) Draw (iii) Check (iv) Valid move (V)
    """

    def __init__(self, board):
        self.board = board
        self.previous = None
        self.count = 0

        pass
    
    def board_state(self):
        pass

    pass
