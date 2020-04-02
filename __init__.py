# Encoding: utf-8

from tkinter import Tk, Canvas, Button
from random import randint


class Snake:

    TITLE = 'Snake by Rim'
    BODY_W = 800
    BODY_H = 600
    BODY_BG = '#000000'
    PIX = 10
    PIX_BG = '#ffffff'
    FOOD_BG = '#889900'
    BUTTON_COLOR = '#ffffff'
    BUTTON_FONT = ('Tahoma', 24, 'bold')
    ERROR_COLOR = '#cc0000'
    ERROR_FONT = ('Tahoma', 18)
    MOVES = {
        'Left': {'x': -1, 'y': 0},
        'Up': {'x': 0, 'y': -1},
        'Right': {'x': 1, 'y': 0},
        'Down': {'x': 0, 'y': 1}
    }
    MOVE = 'Right'

    def __init__(self):
        self.endgame = True
        self.timeout = 100
        self.pixels = []
        self.pixels_coords = []
        self._createWindow()

    def _createWindow(self):
        self.root = Tk()
        self.root.title(self.TITLE)

        self.body = Canvas(self.root, width=self.BODY_W,
                           height=self.BODY_H, bg=self.BODY_BG)
        self.body.grid()
        self.body.focus_set()

    def _generatePixels(self, count):
        for i in range(count):
            pix = self._createPixel(x=(i+1) * self.PIX)
            self.pixels.append(pix)

    def _createElement(self, x, y, fill):
        return self.body.create_rectangle(x, y, x + self.PIX, y + self.PIX, fill=fill)

    def _createPixel(self, x=10, y=10):
        return self._createElement(x, y, self.PIX_BG)

    def _gameCreate(self, e):
        self.endgame = False
        self.body.itemconfig(self.text_error, state='hidden')
        self.body.itemconfig(self.text_start, state='hidden')
        self._generatePixels(3)
        self.MOVE = 'Right'

        self._game()

    def _game(self):
        self._move()
        if self.endgame != True:
            self.root.after(self.timeout, self._game)

    def _move(self):
        if self.endgame != True:
            self.pixels_coords = []
            self._generateFood()
            for i in range(len(self.pixels)):
                try:
                    # Наступний елемент
                    x1, y1, x2, y2 = self.body.coords(self.pixels[i + 1])
                    self.body.coords(self.pixels[i], x1, y1, x2, y2)
                except IndexError as e:
                    # Голови
                    moves = self.MOVES[self.MOVE]
                    x1 = x1 + self.PIX * moves['x']
                    y1 = y1 + self.PIX * moves['y']
                    self.body.coords(
                        self.pixels[i], x1, y1, x1 + self.PIX, y1 + self.PIX)
                    self._endGame()

                self.pixels_coords.append(
                    '{x}x{y}'.format(x=int(x1), y=int(y1)))

    def _moveChange(self, e):
        if e.keysym in ['Left', 'Up', 'Right', 'Down']:
            self.MOVE = e.keysym

    def _generateFood(self):
        rand_row = randint(1, self.BODY_H // self.PIX) * self.PIX
        rand_col = randint(1, self.BODY_W // self.PIX) * self.PIX
        food_coords = f'{rand_col}x{rand_row}'
        if food_coords in self.pixels_coords:
            self._generateFood()
        else:
            self._createElement(rand_col, rand_row, self.FOOD_BG)

    def _endGame(self):
        # Визначаємо позицію голови
        x1, y1, x2, y2 = self.body.coords(self.pixels[-1])
        if x1 < 0 or x1 >= self.BODY_W or y1 < 0 or y1 >= self.BODY_H:
            for pix in self.pixels:
                self.body.delete(pix)
            self.pixels = []
            self.endgame = True
            self.body.itemconfig(self.text_error, state='normal')
            self.body.itemconfig(self.text_start, state='normal')

    def _start(self):
        self.text_error = self.body.create_text(
            self.BODY_W/2, self.BODY_H/2, text='Ви програли!', fill=self.ERROR_COLOR, font=self.ERROR_FONT, state='hidden')
        self.text_start = self.body.create_text(
            self.BODY_W/2, self.BODY_H/2.15, text='Почати гру', fill=self.BUTTON_COLOR, font=self.BUTTON_FONT)
        self.body.tag_bind(self.text_start, '<Button-1>', self._gameCreate)
        self.body.bind("<KeyPress>", self._moveChange)

    def run(self):
        self._start()
        self.root.mainloop()


if __name__ == "__main__":
    Snake().run()
