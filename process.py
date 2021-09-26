import tkinter as tk
from tkinter import *
win = Tk()
fg = Tk()
Label(win, text="hello").pack()
Label(fg, text="hi").pack()
win.mainloop()
fg.mainloop()

"""class createFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        ttk.Button(self, text="hello").pack()
        self.columnconfigure(1, weight=1)
class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        ttk.Label(self, text="helo").grid(row=0, column=0)
        createFrame(self).grid(row=1, column=0)

if __name__ == "__main__":
    app = Application()
    app.mainloop()"""
