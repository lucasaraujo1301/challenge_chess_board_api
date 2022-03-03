import re
from .constants import possible_movements_knight


class Movements:
    """
    A Class to solve the movements of chess pieces
    """

    def __init__(self, piece, position):
        self.piece = piece
        self.position = position
        self.first_turn_movements = []

    def algebraic_notation_to_number(self):
        algebraic_notation = re.findall(r'[a-zA-Z]|\d', self.position)
        x, y = algebraic_notation

        if ord(x.lower()) - 96 > 0:
            x, y = ord(x.lower()) - 96, int(y)
        else:
            x, y = ord(y.lower()) - 96, int(x)

        return x, y

    @staticmethod
    def number_to_algebraic_notation(x_axis, y_axis):
        return "".join((chr(x_axis + 96).upper(), str(y_axis)))

    @staticmethod
    def concat_first_and_second_turn(first_turn, second_turn):
        return f'{first_turn} -> {second_turn}'

    def get_first_turn_movements(self, algebraic_notation, possible_movements):
        first_turn_movements = []

        for possible_movement in possible_movements:
            x, y = algebraic_notation
            w, z = possible_movement

            if 1 <= x + w <= 8 and 1 <= y + z <= 8:
                new_movements_1_turn = x + w, y + z
                self.first_turn_movements.append(new_movements_1_turn)

                # Transforming tuple into string with letter on X axis
                # And appending on all_movements to return
                x_1_turn, y_1_turn = new_movements_1_turn
                first_turn_movements.append(self.number_to_algebraic_notation(x_1_turn, y_1_turn))

        return first_turn_movements

    def get_second_turn_movements(self, possible_movements):
        second_turn_movements = []

        for movement_1_turn in self.first_turn_movements:
            for possible_movement in possible_movements:
                x_1_turn, y_1_turn = movement_1_turn
                w, z = possible_movement

                movements_1_turn_knight_string = self.number_to_algebraic_notation(x_1_turn, y_1_turn)

                if 1 <= x_1_turn + w <= 8 and 1 <= y_1_turn + z <= 8:
                    new_movements_2_turn = x_1_turn + w, y_1_turn + z
                    x_2_turn, y_2_turn = new_movements_2_turn

                    # Transforming tuple into string with letter on X axis and concatenate the movements from
                    # first turn and appending on all_movements to return
                    new_movements_2_turn_string = self.number_to_algebraic_notation(x_2_turn, y_2_turn)
                    new_movements_2_turn_string = self.concat_first_and_second_turn(movements_1_turn_knight_string,
                                                                                    new_movements_2_turn_string)

                    second_turn_movements.append(new_movements_2_turn_string)

        return second_turn_movements

    def calculate_knight_moves(self):
        """
        A function that calculate the Knight's moves on the chessboard in 2 turns
        """
        try:
            x, y = self.algebraic_notation_to_number()

            if x > 8 or y > 8 or x < 1 or y < 1:
                return {'status': 402, 'message': 'Insert existing positions on the 8x8 board'}

            algebraic_notation = x, y

            all_movements = {
                'first_turn': [],
                'second_turn': []
            }

            first_turn_movements = self.get_first_turn_movements(algebraic_notation, possible_movements_knight)
            all_movements['first_turn'].extend(first_turn_movements)

            second_turn_movements = self.get_second_turn_movements(possible_movements_knight)
            all_movements['second_turn'].extend(second_turn_movements)

            return all_movements
        except Exception as e:
            return str(e)
