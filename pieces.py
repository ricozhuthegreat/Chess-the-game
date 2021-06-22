
class Position():

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Piece():

    def __init__(self, position, color):
        self.position = position
        self.color = color

    def move(self, n_position, capture):
        if (check_move_legal(n_position, capture)):
            self.position = n_position

    def check_move_legal(self, n_position, capture):
        pass

class Pawn(Piece):

    def __init__(self, position, color):
        super(Pawn, self).__init__(position, color)
        # Track if it is the first move
        self.first = True
        self.value = 1
        self.type = "P"

    def move(self, n_position, capture):
        if check_move_legal(n_position):
            self.position = n_position

    def check_move_legal(self, n_position, capture):
        if self.first:
            if abs(n_position.y - self.position.y) <= 2 and n_position.x == self.position.x:
                self.first = False
                return True
        elif not self.first and not capture:
            if abs(n_position.y - self.position.y) == 1 and n_position.x == self.position.x:
                return True
        elif not self.first and capture:
            if abs(n_position.y - self.position.y) == 1 and abs(n_position.x - self.position.x) == 1:
                return True
        return False
