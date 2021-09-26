from tkinter import *
import tkinter
win = Tk()
list = [StringVar()]
lst = ["5", "10", "25", "500", "2"]
for i in range(5):
    dc = StringVar()
    dc.set(lst[i])
    list.append(dc)
for i in range(5):
    print(i)
    Entry(win, textvariable=list[i+1]).grid(row=0, column=i)
def df():
    list[1].set("50")
Button(win, text="hello",command=df).grid(rowspan=5)
win.mainloop()