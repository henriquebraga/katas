

class Board:


    def __init__(self):
        self._squares = [['_']  * 10 for line in range(10)]


    def __len__(self):
        return 100


class Game:

    boards = {
        'p1': Board(),
        'p2': Board()
    }

    ships = {
        'aircraft_carrier': 5,
        'cuirassed': 4,
        'submarine': 3,
        'destroyer': 2,
        'patrol' : 2,
    }

    ship_directions = {
        'v': 'vertical',
        'h': 'horizontal',
    }

    def place_ship(self, ship, direction, start_point, player):
        line = self.boards[player]._squares[int(start_point[1])]
        for n in range(5):
            line[n] = ship










