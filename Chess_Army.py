class Piece:  # Acts as the abstract base class [What is constant amongst all pieces]
    selected_piece = False

    def __init__(self, row, col, color):  # Initializing Function
        self.row = row
        self.col = col
        self.color = color

    def movement(self, target):  # Legally Defined Moves
        #  returns a bool value to denote if a move is valid or not
        pass


class Pawns(Piece):  # The Backbone of the Game
    number_moves = 0  # This value is incremented after a pawn moves
    double_kicked: bool = False

    def movement(self, target):
        row2 = target[0]
        col2 = target[1]
        col = target[3]

        # No absolute value for row and col difference cause Pawns can NEVER!! move backwards
        row_diff = row2 - self.row
        col_diff = col2 - self.col

        if self.number_moves == 0 and row_diff == 2 and col_diff == 0:  # Moving twice on first move
            self.double_kicked = True
            self.number_moves += 1
            return self.double_kicked

        elif row_diff == 1 and col_diff == 0:  # The pawn race
            self.number_moves += 1
            return True

        else:
            return False

        # Taking double move, En pass ant and promotion into consideration (some errors with the pawn movement still
        # exist

        # Also need to reformat the pawn class such that whites orientation differs from black
        # i.e: black starts on row 7 and goes forward, while white starts at 0 and goes forward


# Absolute value is needed for all pieces except the pawns

class Knight(Piece):  # The tricky L shaped jumpers
    symbol = 'N'

    def movement(self, target):
        row2 = target[0]
        col2 = target[1]

        row_diff = abs(row2 - self.row)
        col_diff = abs(col2 - self.col)

        piece_slope = col_diff / row_diff

        if (piece_slope == 2 or piece_slope == 0.5) and (row_diff <= 2 and col_diff <= 2):
            return True
        else:
            return False

        pass


class Bishop(Piece):  # Bishops travel  Diagon Alley!
    symbol = 'B'

    def movement(self, target):
        row2 = target[0]
        col2 = target[1]

        row_diff = row2 - self.row
        col_diff = col2 - self.col

        piece_slope = abs(col_diff / row_diff)

        if piece_slope == 1:
            return True
        else:
            return False


class Rook(Piece):  # Horizontal and vertical Guardians
    sacred_symbol = 'R'
    moved_already = False  # determines if the king can castle in the side of the rook

    def movement(self, target):
        row2 = target[0]
        col2 = target[1]

        row_diff = abs(row2 - self.row)
        col_diff = abs(col2 - self.col)

        if (row_diff == 0 and col_diff > 0) or (col_diff == 0 and row_diff > 0):
            return True
        else:
            return False

        pass


class Queen(Piece):  # The most powerful force  (Combo of Bishop and Rook)
    symbol = 'Q'

    def movement(self, target):
        row2 = target[0]
        col2 = target[1]

        row_diff = abs(row2 - self.row)
        col_diff = abs(col2 - self.col)

        piece_slope = col_diff / row_diff

        if (row_diff == 0 and col_diff > 0) or (col_diff == 0 and row_diff > 0) or piece_slope == 1:
            return True
        else:
            return False


class King(Piece):  # The most fragile of them all!
    sacred_symbol = 'K'
    moved_already = False  # determines if the king can castle

    def movement(self, target):
        row2 = target[0]
        col2 = target[1]

        row_diff = abs(row2 - self.row)
        col_diff = abs(col2 - self.col)

        if (col_diff <= 1 and row_diff == 1) or (row_diff <= 1 and col_diff == 1):
            return True

    def king_safety(self, board):
        pass

    def castling(self, board):
        pass
