"""выполнена база и пункты 2, 4, 6, 7"""

class ChessPiece:
    """Базовый класс для всех шахматных фигур."""

    def __init__(self, color, position):
        """
        Инициализирует шахматную фигуру.

        :param color: Цвет фигуры ('white' или 'black').
        :param position: Позиция фигуры на доске в виде кортежа (x, y).
        """
        self.color = color
        self.position = position

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для фигуры.

        :param board: Объект доски, на которой находится фигура.
        :return: Список возможных ходов в виде кортежей (x, y).
        """
        raise NotImplementedError("Subclasses should implement this method")

    def __str__(self):
        """
        Возвращает строковое представление фигуры.

        :return: Символ фигуры в верхнем регистре для белых и в нижнем для черных.
        """
        symbol = self.symbol()
        return symbol.upper() if self.color == 'white' else symbol.lower()

    def symbol(self):
        """
        Возвращает символ фигуры.

        :return: Символ фигуры.
        """
        raise NotImplementedError("Subclasses should implement this method")


class Pawn(ChessPiece):
    """Класс, представляющий пешку."""

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для пешки.

        :param board: Объект доски, на которой находится пешка.
        :return: Список возможных ходов в виде кортежей (x, y).
        """
        moves = []
        direction = 1 if self.color == 'white' else -1
        start_row = 1 if self.color == 'white' else 6
        x, y = self.position

        if board.is_empty((x + direction, y)):
            moves.append((x + direction, y))
            if x == start_row and board.is_empty((x + 2 * direction, y)):
                moves.append((x + 2 * direction, y))

        for dy in [-1, 1]:
            if board.is_opponent((x + direction, y + dy), self.color):
                moves.append((x + direction, y + dy))

        return moves

    def symbol(self):
        """
        Возвращает символ пешки.

        :return: Символ пешки.
        """
        return 'P'


class Rook(ChessPiece):
    """Класс, представляющий ладью."""

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для ладьи.

        :param board: Объект доски, на которой находится ладья.
        :return: Список возможных ходов в виде кортежей (x, y).
        """
        moves = []
        x, y = self.position

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board.is_empty((nx, ny)):
                    moves.append((nx, ny))
                elif board.is_opponent((nx, ny), self.color):
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy

        return moves

    def symbol(self):
        """
        Возвращает символ ладьи.
        :return: Символ ладьи.
        """
        return 'R'


class Knight(ChessPiece):
    """Класс, представляющий коня."""

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для коня.

        :param board: Объект доски, на которой находится конь.
        :return: Список возможных ходов в виде кортежей (x, y).
        """
        moves = []
        x, y = self.position

        for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1),
                       (1, 2), (1, -2), (-1, 2), (-1, -2)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 8 and 0 <= ny < 8 and (board.is_empty((nx, ny)) or board.is_opponent((nx, ny), self.color)):
                moves.append((nx, ny))

        return moves

    def symbol(self):
        """
        Возвращает символ коня.

        :return: Символ коня.
        """
        return 'N'


class Bishop(ChessPiece):
    """Класс, представляющий слона."""

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для слона.

        :param board: Объект доски, на которой находится слон.
        :return: Список возможных ходов в виде кортежей (x, y).
        """
        moves = []
        x, y = self.position

        for dx, dy in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board.is_empty((nx, ny)):
                    moves.append((nx, ny))
                elif board.is_opponent((nx, ny), self.color):
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy

        return moves

    def symbol(self):
        """
        Возвращает символ слона.

        :return: Символ слона.
        """
        return 'B'


class Queen(ChessPiece):
    """Класс, представляющий ферзя."""

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для ферзя.

        :param board: Объект доски, на которой находится ферзь.
        :return: Список возможных ходов в виде кортежей (x, y).
        """
        moves = []
        x, y = self.position

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1),
                        (1, 1), (1, -1), (-1, 1), (-1, -1)]:
            nx, ny = x + dx, y + dy
            while 0 <= nx < 8 and 0 <= ny < 8:
                if board.is_empty((nx, ny)):
                    moves.append((nx, ny))
                elif board.is_opponent((nx, ny), self.color):
                    moves.append((nx, ny))
                    break
                else:
                    break
                nx += dx
                ny += dy

        return moves

    def symbol(self):
        """
        Возвращает символ ферзя.

        :return: Символ ферзя.
        """
        return 'Q'


class King(ChessPiece):
    """Класс, представляющий короля."""

    def get_possible_moves(self, board):
        """
        Возвращает список возможных ходов для короля.

        :param board: Объект доски, на которой находится король.
        :return: Список возможных ходов в виде кортежей (x, y).
        """
        moves = []
        x, y = self.position

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < 8 and 0 <= ny < 8 and (board.is_empty((nx, ny)) or board.is_opponent((nx, ny), self.color)):
                    moves.append((nx, ny))

        return moves

    def symbol(self):
        """
        Возвращает символ короля.

        :return: Символ короля.
        """
        return 'K'


class Board:
    """Класс, представляющий шахматную доску."""

    def __init__(self):
        """Инициализирует пустую шахматную доску."""
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.history = []

    def place_piece(self, piece, position):
        """
        Размещает фигуру на доске.

        :param piece: Фигура, которую нужно разместить.
        :param position: Позиция на доске в виде кортежа (x, y).
        """
        x, y = position
        self.board[x][y] = piece
        piece.position = position

    def is_empty(self, position):
        """
        Проверяет, пуста ли клетка на доске.

        :param position: Позиция на доске в виде кортежа (x, y).
        :return: True, если клетка пуста, иначе False.
        """
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] is None

    def is_opponent(self, position, color):
        """
        Проверяет, находится ли на клетке фигура противника.

        :param position: Позиция на доске в виде кортежа (x, y).
        :param color: Цвет текущей фигуры.
        :return: True, если на клетке фигура противника, иначе False.
        """
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8 and self.board[x][y] is not None and self.board[x][y].color != color

    def move_piece(self, from_pos, to_pos):
        """
        Перемещает фигуру с одной клетки на другую.

        :param from_pos: Начальная позиция фигуры в виде кортежа (x, y).
        :param to_pos: Конечная позиция фигуры в виде кортежа (x, y).
        :return: True, если ход выполнен успешно, иначе False.
        """
        from_x, from_y = from_pos
        to_x, to_y = to_pos
        piece = self.board[from_x][from_y]
        if piece is None:
            return False

        if to_pos not in piece.get_possible_moves(self):
            return False

        self.board[to_x][to_y] = piece
        self.board[from_x][from_y] = None
        piece.position = to_pos
        self.history.append((from_pos, to_pos))
        return True

    def undo_move(self):
        """Отменяет последний ход."""
        if self.history:
            from_pos, to_pos = self.history.pop()
            piece = self.board[to_pos[0]][to_pos[1]]
            self.board[from_pos[0]][from_pos[1]] = piece
            self.board[to_pos[0]][to_pos[1]] = None
            piece.position = from_pos

    def __str__(self):
        """
        Возвращает строковое представление доски.

        :return: Строковое представление доски.
        """
        board_str = "  a b c d e f g h\n"
        for i in range(8):
            row = [str(self.board[i][j]) if self.board[i][j] else '.' for j in range(8)]
            board_str += f"{8 - i} {' '.join(row)}\n"
        return board_str


class Game:
    """Класс, представляющий шахматную игру."""

    def __init__(self):
        """Инициализирует новую шахматную игру."""
        self.board = Board()
        self.setup_board()

    def setup_board(self):
        """Расставляет фигуры на доске в начальную позицию."""
        for i in range(8):
            self.board.place_piece(Pawn('white', (1, i)), (1, i))
            self.board.place_piece(Pawn('black', (6, i)), (6, i))

        self.board.place_piece(Rook('white', (0, 0)), (0, 0))
        self.board.place_piece(Rook('white', (0, 7)), (0, 7))
        self.board.place_piece(Rook('black', (7, 0)), (7, 0))
        self.board.place_piece(Rook('black', (7, 7)), (7, 7))

        self.board.place_piece(Knight('white', (0, 1)), (0, 1))
        self.board.place_piece(Knight('white', (0, 6)), (0, 6))
        self.board.place_piece(Knight('black', (7, 1)), (7, 1))
        self.board.place_piece(Knight('black', (7, 6)), (7, 6))

        self.board.place_piece(Bishop('white', (0, 2)), (0, 2))
        self.board.place_piece(Bishop('white', (0, 5)), (0, 5))
        self.board.place_piece(Bishop('black', (7, 2)), (7, 2))
        self.board.place_piece(Bishop('black', (7, 5)), (7, 5))

        self.board.place_piece(Queen('white', (0, 3)), (0, 3))
        self.board.place_piece(Queen('black', (7, 3)), (7, 3))

        self.board.place_piece(King('white', (0, 4)), (0, 4))
        self.board.place_piece(King('black', (7, 4)), (7, 4))

    def play(self):
        """Запускает шахматную игру."""
        turn = 'white'
        while True:
            print(self.board)
            print(f"{turn}'s turn")
            from_pos = input("Enter the position of the piece to move (e.g., 'a2'): ")
            to_pos = input("Enter the target position (e.g., 'a3'): ")

            from_pos = self.parse_position(from_pos)
            to_pos = self.parse_position(to_pos)

            if self.board.is_empty(from_pos):
                print("No piece at the specified position")
                continue

            piece = self.board.board[from_pos[0]][from_pos[1]]
            if piece.color != turn:
                print("It's not your piece")
                continue

            if not self.board.move_piece(from_pos, to_pos):
                print("Invalid move")
                continue

            turn = 'black' if turn == 'white' else 'white'

    def parse_position(self, pos):
        """
        Преобразует шахматную нотацию в координаты доски.

        :param pos: Позиция в шахматной нотации (например, 'a2').
        :return: Координаты позиции в виде кортежа (x, y).
        """
        x = 8 - int(pos[1])
        y = ord(pos[0]) - ord('a')
        return (x, y)


if __name__ == "__main__":
    game = Game()
    game.play()