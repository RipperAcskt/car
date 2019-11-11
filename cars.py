from pygame import time

class car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, speed):
        self.y += speed


