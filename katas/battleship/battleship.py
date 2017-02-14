

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

    def place_ship(self, ship, position, player, direction='h'):
        column_no, line_no = (int(coordinate) for coordinate in position)
        line = self.boards[player]._squares[column_no]
        SHIP_POSITION = slice(0, self.get_ship_size(ship), None)

        line[SHIP_POSITION] = [ship] * self.get_ship_size(ship)

    def get_ship_size(self, key):
        return self.ships.get(key)











