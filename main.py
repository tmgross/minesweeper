from minesweeper import *
import tkinter as tk

def main():
    win = tk.Tk()
    ms = minesweeper(win, 5, 5, 10)
    ms.initialize_grid()

    win.mainloop()


if __name__ == '__main__':
    main()