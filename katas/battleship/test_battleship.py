from unittest import TestCase


from katas.battleship.battleship import Board, Game


class BoardTest(TestCase):


    def setUp(self):
        self.board = Board()

    def test_board_should_have_100_positions(self):
        self.assertEquals(100, len(self.board))

    def test_board_should_have_init(self):
        self.assertTrue(getattr(self.board, '__init__'))

    def test_board_should_have_ten_lines(self):
        self.assertEquals(10, len(self.board._squares))


class GameTest(TestCase):

    def setUp(self):
        self.game = Game()
        self.board_p1 = self.game.boards['p1']


    def test_game_should_have_five_ships(self):
        self.assertEqual(5, len(self.game.ships))

    def test_carrier_should_have_five_length(self):
        self.assertEquals(5, self.game.ships['aircraft_carrier'])

    def test_cuirassed_should_have_four_length(self):
        self.assertEquals(4, self.game.ships['cuirassed'])

    def test_submarine_should_have_three_length(self):
        self.assertEquals(3, self.game.ships['submarine'])

    def test_destroyer_should_have_two_length(self):
        self.assertEquals(2, self.game.ships['destroyer'])

    def test_patrol_should_have_two_length(self):
        self.assertEquals(2, self.game.ships['patrol'])

    def test_game_should_have_two_boards(self):
        self.assertEquals(2, len(self.game.boards))

    def test_ships_should_have_vertical_and_horizontal_directions_to_place(self):
        expected = dict(v='vertical', h='horizontal')
        self.assertDictEqual(expected, self.game.ship_directions )

    def test_when_p1_place_an_aircraft_carrier_positions_should_be_changed(
       self):

        self.game = Game()
        self.game.place_ship(
                            ship='aircraft_carrier',
                            direction='v',
                            position='00',
                            player='p1'
                             )
        expected = ['aircraft_carrier'] * 5 + ['_'] * 5
        self.assertSequenceEqual(expected, self.board_p1._squares[0][:])

    def test_when_p1_place_a_cuirassed_positions_should_be_changed(self):
        self.game.boards['p1'] = Board()

        self.game.place_ship(
                    ship='cuirassed',
                    direction='h',
                    position='00',
                    player='p1'
                    )

        expected = ['cuirassed'] * 4 + ['_', '_', '_', '_', '_', '_']
        self.assertSequenceEqual(expected, self.game.boards['p1']._squares[0][:])

    def test_when_p1_place_a_patrol_in_second_column_it_should_be_changed(self):
        self.game.boards['p1'] = Board()

        self.game.place_ship(
            ship='patrol',
            direction='h',
            position='10',
            player='p1'
        )

        expected = ['patrol'] * 2 + ['_', '_', '_', '_', '_', '_', '_', '_']
        self.assertSequenceEqual(expected, self.game.boards['p1']._squares[1][:])

    