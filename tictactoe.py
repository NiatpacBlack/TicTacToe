from tkinter import Canvas, Tk
from random import randint


class TicTacToe(Canvas):

    def __init__(self, window_object):
        """ Переопределяем конструктор Canvas, фиксируем размеры поля и определяем клетки, статус нажатия и победы """

        super().__init__(window_object, width=295, height=295, bg='dark sea green')
        self.state = {
            (0, 0): 'None', (0, 1): 'None', (0, 2): 'None', (1, 0): 'None', (1, 1): 'None', (1, 2): 'None',
            (2, 0): 'None', (2, 1): 'None', (2, 2): 'None'
        }
        self.bind('<Button-1>', self.click)
        self.winner = 'None'

    def draw_lines(self):
        """ Отрисовка сетки поля """

        for iteration in range(1, 3):
            self.create_line(100 * iteration, 0, 100 * iteration, 300, fill='white')
            self.create_line(0, 100 * iteration, 300, 100 * iteration, fill='white')

    def draw_win_area(self):
        """ Отрисовка поля после победы """

        self.create_rectangle(0, 0, 295, 295, fill='white')
        if self.winner == 'Вы победили':
            self.create_text(150, 100, fill="lime", font="Roboto 25 bold",
                             text=self.winner)
        elif self.winner == 'Вы проиграли':
            self.create_text(150, 100, fill="red", font="Roboto 25 bold",
                             text=self.winner)
        elif self.winner == 'Ничья':
            self.create_text(150, 100, fill="darkblue", font="Roboto 25 bold",
                             text=self.winner)

    def add_x(self, column=0, row=0):
        """ Отрисовка крестика """

        coordinates = [[20, 80], [80, 20]]
        for coordinate in coordinates:
            self.create_line(
                coordinate[0] + 100 * column,
                20 + 100 * row,
                coordinate[1] + 100 * column,
                80 + 100 * row,
                width=5,
                fill='blue'
            )

    def add_o(self, column=0, row=0):
        """ Отрисовка нолика """

        self.create_oval(
            20 + 100 * column,
            20 + 100 * row,
            80 + 100 * column,
            80 + 100 * row,
            width=5,
            outline='red'
        )

    def click(self, event):
        """ Обработка нажатия игрока """

        position_x = event.x // 100
        position_y = event.y // 100

        if self.state[(position_x, position_y)] == 'None':
            self.add_x(position_x, position_y)
            self.state[(position_x, position_y)] = 'x'
            self.enemy_click()
            self.get_winner()

    def enemy_click(self):
        """ Ответная отрисовка нолика """

        free_cells = [keys for keys in self.state.keys() if self.state[keys] == 'None']

        if len(free_cells) != 0:
            coordinates = free_cells[randint(0, len(free_cells) - 1)]
            position_x = coordinates[0]
            position_y = coordinates[1]
            self.add_o(position_x, position_y)
            self.state[(position_x, position_y)] = 'o'
            self.get_winner()

    def get_winner(self):
        """ Проверка на соответствие победным значениям """

        list_cells = [val for val in self.state.values()]
        winner_x = ['x', 'x', 'x']
        winner_o = ['o', 'o', 'o']
        win_combo = [
            list_cells[0:3], list_cells[3:6], list_cells[6:9], list_cells[0:7:3], list_cells[1:8:3],
            list_cells[2:9:3], list_cells[0:9:4], list_cells[2:7:2]
        ]
        if winner_x in win_combo:
            self.winner = 'Вы победили'
            self.draw_win_area()
        elif winner_o in win_combo:
            self.winner = 'Вы проиграли'
            self.draw_win_area()
        elif 'None' not in self.state.values():
            self.winner = 'Ничья'
            self.draw_win_area()


if __name__ == '__main__':
    window = Tk()
    window.title('TicTacToe')
    window.geometry('295x295')
    window.resizable(width=False, height=False)
    game = TicTacToe(window)
    game.pack()
    game.draw_lines()
    window.mainloop()
