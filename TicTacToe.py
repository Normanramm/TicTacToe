import tkinter
import random


class TicTacToe(tkinter.Canvas):  # Крестики-нолики
    def __init__(self, window):
        super().__init__(window, width=300, height=300)
        self.state = [
                         None, ] * 9  # Ходим первыми(хранить состояние игры, значение None будет обозначать то, что ячейка свободна)
        self.bind('<Button-1>', self.click)

    def get_winner(self):  # Кто победил?
        lines = [
            self.state[0:3], self.state[3:6], self.state[6:9],  # по горизонтали
            self.state[0:9:3], self.state[1:9:3], self.state[2:9:3],  # по вертикали
            self.state[0:9:4], self.state[2:7:2]  # по диагонали
        ]

        if ['x'] * 3 in lines:
            return 'x_win'
        elif ['o'] * 3 in lines:
            return 'o_win'
        elif None not in self.state:
            return 'draw'

    def bot_move(self):  # Глупый бот(создание бота, который будет играть против нас)
        index = random.choice([index for index, e in enumerate(self.state) if e is None])
        self.state[index] = 'o'
        self.add_o(column=index % 3, row=int(index / 3))

    def click(self, event):  # Ходим первыми(метод-обработчик клика по холсту)
        column = event.x // 100
        row = event.y // 100
        index = row * 3 + column
        if self.state[index] is None:
            self.state[index] = 'x'
            self.add_x(column, row)
            pobeda = self.get_winner()
            if pobeda:
                self.pobedaPobeda(pobeda)
                self.deleteDelete()
            else:
                self.bot_move()  # обработчик клика
                pobeda = self.get_winner()
                if pobeda:
                    self.pobedaPobeda(pobeda)
                    self.deleteDelete()

    def pobedaPobeda(self, pobeda):  # Собираем все вместе(тут должна быть информация о победителе)
        self.create_text(150, 150, text=f"{pobeda} победил!", font=("Arial", 24), fill="green")
        self.deleteDelete()

    def deleteDelete(self):  # Собираем все вместе(очистить холст)
        self.delete("all")
        self.state = [None] * 9
        self.draw_lines()

    def add_x(self, column, row):  # Рисуем(кресты)
        self.create_line(column * 100 + 20, row * 100 + 20, column * 100 + 80, row * 100 + 80, fill="red", width=3)
        self.create_line(column * 100 + 80, row * 100 + 20, column * 100 + 20, row * 100 + 80, fill="red", width=3)

    def add_o(self, column, row):  # Рисуем(круг)
        self.create_oval(column * 100 + 20, row * 100 + 20, column * 100 + 80, row * 100 + 80, width=5, outline='blue')

    def draw_lines(self):  # Рисуем линии
        self.create_line(100, 0, 100, 300, fill="black", width=2)
        self.create_line(200, 0, 200, 300, fill="black", width=2)
        self.create_line(0, 100, 300, 100, fill="black", width=2)
        self.create_line(0, 200, 300, 200, fill="black", width=2)


okno = tkinter.Tk()
game = TicTacToe(okno)
game.pack()

# game.add_o(0, 2)  # рисует круг
# game.add_x(column=0, row=0)  # рисует крест

game.draw_lines()  # создает линии

okno.mainloop()
