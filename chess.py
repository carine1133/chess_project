class Pieces:
    """Базовый класс для всех шахматных фигур.

      Содержит общие свойства и методы для всех типов фигур:
      - координаты положения
      - цвет фигуры
      - статус (активна/уничтожена)
      - базовые методы перемещения и проверки ходов
      """
    def __init__(self, x, y, color):
        """Инициализация базовых свойств шахматной фигуры.

              Args:
                  x (int): Начальная координата по горизонтали (0-7, где 0 - крайняя левая)
                  y (int): Начальная координата по вертикали (0-7, где 0 - верхний ряд)
                  color (str): Цвет фигуры ('w' - белые, 'b' - черные)
              """
        self.x = x
        self.y = y
        self.color = color
        self.status = True

    def destroy(self):
        """Помечает фигуру как уничтоженную.

              Устанавливает статус фигуры в False и выводит сообщение об уничтожении.
              Фигура остается в памяти, но исключается из игрового процесса.
              """
        self.status = False
        print(f"Фигура {self.name} уничтожена")

    def move(self, x, y):
        """Перемещает фигуру на указанные координаты.

               Args:
                   x (int): Новая координата по горизонтали
                   y (int): Новая координата по вертикали
               """
        self.x = x
        self.y = y

    def __str__(self):
        """Возвращает строковое представление фигуры.

              Returns:
                  str: Первая буква названия фигуры (строчная для белых, заглавная для черных)
              """
        return self.name[0]

    def chek_move(self, x, y, board):
        """Абстрактный метод проверки допустимости хода.

                Должен быть реализован в дочерних классах для каждого типа фигур.

                Args:
                    x (int): Целевая координата по горизонтали
                    y (int): Целевая координата по вертикали
                    board (Board): Объект игровой доски для проверки препятствий

                Returns:
                    bool: True если ход допустим, False если нет
                """
        pass

    def color(self):
        """Возвращает цвет фигуры.

               Returns:
                   str: 'w' для белых фигур, 'b' для черных
               """
        return self.color

class Pawns(Pieces):
    """Класс пешки. Наследуется от базового класса Pieces.

      Особенности:
      - Может двигаться только вперед
      - Первый ход может быть на 2 клетки
      - Бьет по диагонали на одну клетку
      - При достижении противоположного края доски может превращаться в другие фигуры
      """
    def __init__(self, x, y, color):
        """Инициализация пешки.

               Args:
                   x (int): Начальная координата по горизонтали
                   y (int): Начальная координата по вертикали
                   color (str): Цвет фигуры ('w'/'b')
               """
        super().__init__(x, y, color)
        if self.color == 'w':
            self.name = 'pawns'
            self.coef = 1
        else:
            self.name = 'Pawns'
            self.coef = -1

    def chek_move(self, x, y, board):
        """Проверка допустимости хода для пешки.

        Args:
            x (int): Целевая координата по горизонтали
            y (int): Целевая координата по вертикали
            board (Board): Объект игровой доски

        Returns:
            bool: True если ход допустим, False если нет
        """
        if board.board[y][x] == '.' and self.x == x:
            if self.y == 1 or self.y == 6:
                return (self.coef * (y - self.y)) <= 2
            else:
                return (self.coef * (y - self.y)) == 1
        elif  board.board[y][x] != '.' and self.coef * (y - self.y) == 1 and abs(x - self.x) == 1:
            return True
        else:
            return False

class Rooks(Pieces):
    """Класс ладьи. Наследуется от базового класса Pieces.

      Особенности:
      - Может двигаться на любое количество клеток по горизонтали или вертикали
      - Не может перепрыгивать через другие фигуры
      """

    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if self.color == 'w':
            self.name = 'rooks'
        else:
            self.name = 'Rooks'

    def chek_move(self, x, y, board):
        """Проверка допустимости хода для ладьи."""
        if self.x == x:
            for i in range(min(self.y, y) + 1, max(self.y, y)):
                if board.board[i][x] != '.':
                    return False
            return True
        elif self.y == y:
            for i in range(min(self.x, x) + 1, max(self.x, x)):
                if board.board[y][x] != '.':
                    return False
            return True
        else:
            return False

class Horse(Pieces):
    """Класс коня. Наследуется от базового класса Pieces.

     Особенности:
     - Ходит буквой "Г" (2 клетки в одном направлении и 1 в перпендикулярном)
     - Может перепрыгивать через другие фигуры
     """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if self.color == 'w':
            self.name = 'horse'
        else:
            self.name = 'Horse'

    def chek_move(self, x, y, board):
        if ((abs(self.x - x) == 2 and abs(self.y - y) == 1) or
            (abs(self.x - x) == 1 and abs(self.y - y) == 2)):
            return True
        else:
            return False

class Elephant(Pieces):
    """Класс слона. Наследуется от базового класса Pieces.

    Особенности:
    - Может двигаться на любое количество клеток по диагонали
    - Не может перепрыгивать через другие фигуры
    - Всегда остается на клетках одного цвета
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if self.color == 'w':
            self.name = 'elephant'
        else:
            self.name = 'Elephant'

    def chek_move(self, x, y, board):
        if (abs(self.x - x) == abs(self.y - y)):
            for i in range(1, abs(self.y - y)):
                if board.board[self.y + (1 if y > self.y else -1) * i][self.x + (1 if x > self.x else -1) * i] != '.':
                    return False
            return True
        else:
            return False

class King(Pieces):
    """Класс короля. Наследуется от базового класса Pieces.

    Особенности:
    - Может двигаться на одну клетку в любом направлении
    - Не может ходить под шах
    - Имеет право на рокировку (не реализовано в текущей версии)
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if self.color == 'w':
            self.name = 'king'
        else:
            self.name = 'King'

    def chek_move(self, x, y, board):
        if (abs(self.x - x) < 2 and abs(self.y - y) < 2):
            return True
        else:
            return False

class Queen(Pieces):
    """Класс ферзя. Наследуется от базового класса Pieces.

    Особенности:
    - Сочетает возможности ладьи и слона
    - Может двигаться на любое количество клеток по горизонтали, вертикали или диагонали
    - Не может перепрыгивать через другие фигуры
    - Самая мощная фигура на доске
    """
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        if self.color == 'w':
            self.name = 'queen'
        else:
            self.name = 'Queen'

    def chek_move(self, x, y, board):
        if (abs(self.x - x) == abs(self.y - y)):
            for i in range(1, abs(self.y - y)):
                if board.board[self.y + (1 if y > self.y else -1) * i][self.x + (1 if x > self.x else -1) * i] != '.':
                    return False
            return True
        elif self.x == x:
            for i in range(min(self.y, y) + 1, max(self.y, y)):
                if board.board[i][x] != '.':
                    return False
            return True
        elif self.y == y:
            for i in range(min(self.x, x) + 1, max(self.x, x)):
                if board.board[y][x] != '.':
                    return False
            return True
        else:
            return False


class Board():
    """Класс шахматной доски.

    Отвечает за:
    - Хранение состояния всех фигур
    - Валидацию ходов
    - Отображение доски
    - Ведение истории ходов
    - Управление уничтоженными фигурами
    """
    def __init__(self):
        """Инициализация шахматной доски.

         Создает:
         - Пустую доску 8x8
         - Расставляет фигуры в начальные позиции
         - Инициализирует стек ходов и список уничтоженных фигур
         """
        self.board = [['.' for _ in range(8)] for _ in range(8)]
        self.board[1] = [Pawns(i, 1, 'w') for i in range(8)]
        self.board[6] = [Pawns(i, 6, 'b') for i in range(8)]

        self.board[0][0] = Rooks(0, 0, 'w')
        self.board[0][7] = Rooks(7, 0, 'w')
        self.board[7][0] = Rooks(0, 7, 'b')
        self.board[7][7] = Rooks(7, 7, 'b')

        self.board[0][1] = Horse(1, 0, 'w')
        self.board[0][6] = Horse(6, 0, 'w')
        self.board[7][1] = Horse(1, 7, 'b')
        self.board[7][6] = Horse(6, 7, 'b')

        self.board[0][2] = Elephant(2, 0, 'w')
        self.board[0][5] = Elephant(5, 0, 'w')
        self.board[7][2] = Elephant(2, 7, 'b')
        self.board[7][5] = Elephant(5, 7, 'b')

        self.board[0][4] = King(4, 0, 'w')
        self.board[7][4] = King(4, 7, 'b')

        self.board[0][3] = Queen(3, 0, 'w')
        self.board[7][3] = Queen(3, 7, 'b')

        self.steak = Steak()
        self.destroy_figures = []

    def print(self):
        """Выводит текущее состояние доски в консоль.

           Формат вывода:
           - Буквы столбцов (A-H) сверху и снизу
           - Цифры строк (1-8) слева и справа
           - Фигуры обозначаются первой буквой их названия
           """
        print(f'     A  B  C  D  E  F  G  H\n')
        for i in range(1, 9):
            print(f'{i}   ', end = '')
            for j in range(8):
                print(f' {self.board[i - 1][j]}', end = ' ')
            print(f'  {i}')
        print(f'\n     A  B  C  D  E  F  G  H')

    def chek(self, x , y, x_new, y_new):
        """Проверяет допустимость хода для фигуры в указанных координатах.

        Args:
            x (int): Текущая координата x фигуры
            y (int): Текущая координата y фигуры
            x_new (int): Целевая координата x
            y_new (int): Целевая координата y

        Returns:
            bool: True если ход допустим, False если нет
        """
        return self.board[y][x].chek_move(x_new, y_new, self)

    def chek_dot(self, x, y):
        """Проверяет, пуста ли указанная клетка.

          Args:
              x (int): Координата x
              y (int): Координата y

          Returns:
              bool: True если клетка пуста, False если занята
          """
        return self.board[y][x] == '.'

    def move(self, x , y, x_new, y_new):
        """Выполняет перемещение фигуры на доске.

          Args:
              x (int): Текущая координата x
              y (int): Текущая координата y
              x_new (int): Новая координата x
              y_new (int): Новая координата y

          Side effects:
              - Обновляет позицию фигуры
              - При взятии фигуры противника добавляет ее в список уничтоженных
              - Добавляет запись о ходе в историю
          """
        self.steak.app(x, y, self.board[y][x].name, x_new, y_new)
        self.board[y][x].move(x_new, y_new)
        if self.board[y_new][x_new] != '.':
            self.steak.app(x_new, y_new, self.board[y_new][x_new].name, -1, -1)
            self.destroy_figures.append(self.board[y_new][x_new])
            self.board[y_new][x_new].destroy()
        self.board[y_new][x_new] = self.board[y][x]
        self.board[y][x] = '.'

    def move_reverse(self, x , y, x_new, y_new):
        """Отменяет ход (используется для отката игры).

         Args:
             x (int): Координата x фигуры для возврата
             y (int): Координата y фигуры для возврата
             x_new (int): Координата x целевой позиции
             y_new (int): Координата y целевой позиции
         """
        if x != -1:
            self.board[y][x].move(x_new, y_new)
            self.board[y_new][x_new] = self.board[y][x]
            self.board[y][x] = '.'
        else:
            self.board[y_new][x_new] =  self.destroy_figures.pop()


    def chek_color(self, x, y, color):
        """Проверяет соответствие цвета фигуры текущему игроку.

        Args:
            x (int): Координата x фигуры
            y (int): Координата y фигуры
            color (bool): True для белых, False для черных

        Returns:
            bool: True если цвет фигуры соответствует текущему игроку, иначе False
        """
        if ((self.board[y][x].color == "w" and color == True) or
            (self.board[y][x].color == "b" and color == False)):

            return False
        else:
            return True

    def chek_cut_down(self, x , y, x_new, y_new):
        """Проверяет, не пытается ли игрок побить свою же фигуру.

        Args:
            x (int): Координата x исходной фигуры
            y (int): Координата y исходной фигуры
            x_new (int): Координата x цели
            y_new (int): Координата y цели

        Returns:
            bool: True если цель - фигура того же цвета, иначе False
        """
        if self.board[y_new][x_new] == '.':
            return False
        else:
            return self.board[y][x].color == self.board[y_new][x_new].color

class Steak():
    """Класс для хранения истории ходов (стек ходов).

    Позволяет:
    - Сохранять последовательность ходов
    - Отображать историю игры
    - Откатывать игру на несколько ходов назад
    """
    def __init__(self):
        self.steak = []
        self.len = 0

    def app(self, *st):
        """Добавляет ход в историю.

        Args:
            *st: Параметры хода (x, y, имя фигуры, x_new, y_new)
        """
        if st[3] != -1:
            self.len += 1
        self.steak.append(st)

    def print_steak(self):
        """Выводит всю историю ходов в консоль."""
        for i in range(len(self.steak)):
            print(self.steak[i])

    def reverse(self, step, board, motion):
        """Откатывает игру на указанное количество ходов назад.

          Args:
              step (int): Количество ходов для отката
              board (Board): Объект игровой доски
              motion (int): Текущий номер хода

          Returns:
              int: Новый номер хода после отката
          """
        if step > self.len:
            print("Еще не сделано такое большое колличество шагов")
            return motion

        for i in range(step):
            st = self.steak.pop()
            print(st)
            if st[3] == -1:
                st_1 = self.steak.pop()
                board.move_reverse(st_1[3], st_1[4], st_1[0], st_1[1])
            board.move_reverse(st[3], st[4], st[0], st[1])
            print(f"Ход {motion - i - 1}")
            board.print()

        return motion - step

class Play():
    """Основной класс игры, управляющий игровым процессом.

    Отвечает за:
    - Цикл игры
    - Взаимодействие с игроками
    - Координацию работы доски и истории ходов
    """
    def __init__(self):
        self.board = Board()
        self.motion = 0

    def play(self):
        """Основной игровой цикл.

        Обрабатывает:
        - Ввод координат от игроков
        - Проверку допустимости ходов
        - Отображение доски
        - Управление историей ходов
        - Определение очередности ходов
        """
        #  цикл игры
        while True:
            self.board.print()

            print(f'Идет {self.motion + 1} ход') # номер хода

            # перейти к просмотру истории или ее откат
            try:
                history = int(input("1 - Узнать историю игры\n2 - Отмотать шаги назад\n3 - Продолжить играть"))
                assert history > 0 and history < 4
            except (ValueError, AssertionError):
                print("Выбран неверный режим")
                continue

            # вывод истории игры
            if history == 1:
                self.board.steak.print_steak()

            if history == 2:
                try:
                    step = int(input("Введите колличество шагов, на которые хотете вернуться:"))
                except ValueError:
                    print("Некоректно ведено колличество шагов")

                self.motion = self.board.steak.reverse(step, self.board, self.motion)
                continue

            # определяется какой игрок ходит
            if self.motion % 2 == 0:
                print("Ход первого игрока")
            else:
                print("Ход второго игрока")

            # ввод координат фигуры
            try:
                coor_x = ord(input("Введите коррдинату фигуры:")) - ord('A')
                coor_y = int(input("Введите ординату фигуры:")) - 1
                assert coor_x >= 0 and coor_x <= 8
                assert coor_y >= 0 and coor_x <= 7
            except (ValueError, AssertionError):
                print("Кординаты введены не корректно")
                continue

            # проверка, что в данной клетке есть фигура
            if self.board.chek_dot(coor_x, coor_y):
                print("В данной координате нет фигуры. Введите значение снова!")
                continue

            # проверка, что в данной клетке фигура игрока, соверщающего ход
            if self.board.chek_color(coor_x, coor_y, self.motion % 2 == 0):
                print("В данной координате фигура вашего соперника. Введите значение снова!")
                continue

            # ввод новых координат фигуры
            try:
                coor_x_new = ord(input("Введите новую коррдинату фигуры:")) - ord('A')
                coor_y_new = int(input("Введите новую ординату фигуры:")) - 1
                assert coor_x_new >= 0 and coor_x_new <= 8
                assert coor_y_new >= 0 and coor_x_new <= 7
            except (ValueError, AssertionError):
                print("Новые кординаты введены не корректно")
                continue

            # проверка, что за фигуру пытаемся срубить
            if self.board.chek_cut_down(coor_x, coor_y, coor_x_new, coor_y_new):
                print("Нельзя срубить фигуру своего цвета")
                continue

            # проверка на вохиожность движения и само движение
            if self.board.chek(coor_x, coor_y, coor_x_new, coor_y_new):
                self.board.move(coor_x, coor_y, coor_x_new, coor_y_new)
                self.motion += 1
            else:
                print("Фигура не может туда сходить")

game = Play()
game.play()

