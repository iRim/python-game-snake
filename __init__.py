# Encoding: utf-8

import time
from tkinter import Tk, Canvas


class Pixel:

    def __init__(self, x, y):
        self.instance = Canvas.create_rectangle(
            x, y, x + self.SNAKE_PIX, y + self.SNAKE_PIX, fill=self.SNAKE_PIX_BG)


class Snake:

    def __init__(self):
        # global settings
        self.BODY_W = 800
        self.BODY_H = 600
        self.BODY_BG = '#000000'
        self.SNAKE_PIX = 10
        self.SNAKE_PIX_BG = '#ffffff'
        self.SNAKE_PIXELS = []
        self.SNAKE_TIMEOUT = 1
        self._window()

    def _window(self):
        self.root = Tk()
        self.root.title('Snake')

        self._createBody()

    def _createBody(self):
        self.body = Canvas(self.root, width=self.BODY_W,
                           height=self.BODY_H, bg=self.BODY_BG)
        self.body.grid()
        self.body.focus_set()

    def createPix(self, x, y):
        # self.SNAKE_BODY.append(pix)
        return self.body.create_rectangle(
            x, y, x + self.SNAKE_PIX, y + self.SNAKE_PIX, fill=self.SNAKE_PIX_BG)

    def move(self):
        for k, v in enumerate(self.SNAKE_BODY):
            print()

    def timer(self):
        while True:
            self.move()
            # time.sleep(self.SNAKE_TIMEOUT)
            break

    def start(self):
        for p in range(3):
            self.SNAKE_PIXELS.append(Pixel(self.SNAKE_PIX * p, 10))
        self.timer()
        self.root.mainloop()


if __name__ == "__main__":
    s = Snake()
    s.start()
