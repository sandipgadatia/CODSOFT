import unittest
from src.board import check_winner, is_board_full
from src.minimax import find_best_move

class TestTicTacToe(unittest.TestCase):
    def test_check_winner(self):
        board = [
            ['X', 'X', 'X'],
            [' ', 'O', ' '],
            ['O', ' ', ' ']
        ]
        self.assertEqual(check_winner(board), 'X')
        
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', ' '],
            ['O', 'O', 'O']
        ]
        self.assertEqual(check_winner(board), 'O')
        
        board = [
            ['X', 'O', 'X'],
            ['X', 'X', 'O'],
            ['O', 'X', 'O']
        ]
        self.assertIsNone(check_winner(board))

    def test_is_board_full(self):
        board = [
            ['X', 'O', 'X'],
            ['X', 'O', 'O'],
            ['O', 'X', 'X']
        ]
        self.assertTrue(is_board_full(board))

        board = [
            ['X', 'O', 'X'],
            ['X', 'O', ' '],
            ['O', 'X', 'X']
        ]
        self.assertFalse(is_board_full(board))

    def test_find_best_move(self):
        board = [
            ['X', 'O', 'X'],
            ['O', 'X', ' '],
            [' ', ' ', 'O']
        ]
        # Both (2, 0) and (2, 1) are valid optimal moves for this scenario.
        possible_moves = [(2, 0), (2, 1)]
        self.assertIn(find_best_move(board), possible_moves)

if __name__ == '__main__':
    unittest.main()
