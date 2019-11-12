class Game:
    def check_mate(self):  # the necessary conditions for checkmate [Game ends once  true]
        pass

    def draw(self):
        """
        :return: returns a bool value depending on
            1) the kings ability to move and if there's no other pieces that can move
            2) the total number of pieces available (insufficient materials)
            3) "50-move rule": 50 moves without a capture or pawn move
            4) "Repetition rule": A sequence of moves are repeated thrice in any order
            5) draw offer is accepted
        """
        pass


pass
