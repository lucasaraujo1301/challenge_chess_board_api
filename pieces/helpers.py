import re
from .constants import possible_movements_knight


class Movements:
    """
    A Class to solve the movements of chess pieces
    """

    def __init__(self, piece, position):
        self.piece = piece
        self.position = position

    def calculate_knight_moves(self):
        """
        A function that calculate the Knight's moves on the chessboard in 2 turns
        """
        try:
            algebraic_notation = re.findall(r'[a-zA-Z]|\d', self.position)
            x, y = algebraic_notation

            if ord(x.lower()) - 96 > 0:
                x, y = ord(x.lower()) - 96, int(y)
            else:
                x, y = ord(y.lower()) - 96, int(x)

            if x > 8 or y > 8 or x < 1 or y < 1:
                return {'status': 402, 'message': 'Insert existing positions on the 8x8 board'}

            algebraic_notation = x, y

            all_movements = {
                'first_turn': [],
                'second_turn': []
            }
            movements_1_turn_knight = []

            for movement_knight in possible_movements_knight:
                x, y = algebraic_notation
                w, z = movement_knight

                if 1 <= x + w <= 8 and 1 <= y + z <= 8:
                    new_movements_1_turn = x + w, y + z
                    movements_1_turn_knight.append(new_movements_1_turn)

                    # Transforming tuple into string with letter on X axis and with the movements from first turn
                    # And appending on all_movements to return
                    x_1_turn, y_1_turn = new_movements_1_turn
                    new_movements_1_turn_knight_string = "".join((chr(x_1_turn + 96).upper(), str(y_1_turn)))
                    all_movements['first_turn'].append(new_movements_1_turn_knight_string)

            for movement_1_turn_knight in movements_1_turn_knight:
                for movement_knight in possible_movements_knight:
                    x_1_turn, y_1_turn = movement_1_turn_knight
                    w, z = movement_knight

                    movements_1_turn_knight_string = "".join((chr(x_1_turn + 96).upper(), str(y_1_turn)))

                    if 1 <= x_1_turn + w <= 8 and 1 <= y_1_turn + z <= 8:
                        # Transforming tuple into string with letter on X axis and with the movements from first turn
                        # And appending on all_movements to return

                        new_movements_2_turn = chr(x_1_turn + w + 96).upper(), str(y_1_turn + z)
                        new_movements_2_turn = "".join(new_movements_2_turn)
                        new_movements_2_turn_string = f'{movements_1_turn_knight_string} -> {new_movements_2_turn}'

                        all_movements['second_turn'].append(new_movements_2_turn_string)

            return all_movements
        except Exception as e:
            return "The position must be in Algebraic Notation"
