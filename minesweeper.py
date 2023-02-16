import random
import math
import tkinter as tk
from functools import partial


def color_config(widget, color, event):
    widget.configure(bg=color)


class minesweeper:
    def __init__(self, win, width, height, num_mines):
        self.win = win
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.grid = [[tk.Button(self.win) for _ in range(self.width)] for _ in range(self.height)]

        self.colors = {
            'clicked': "#595958",
            'unclicked': "#f8f8ff",
            'hover': "#7D7E8C"
        }

    def initialize_grid(self):
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j].configure(height=5, width=10, text=str(i) + ' ' + str(j), bg=self.colors['unclicked'],
                                          relief='sunken')
                self.grid[i][j].grid(row=i, column=j, sticky=tk.NSEW)
                self.grid[i][j].bind("<Enter>", partial(color_config, self.grid[i][j], self.colors['hover']))
                self.grid[i][j].bind("<Leave>", partial(color_config, self.grid[i][j], self.colors['unclicked']))
