from tkinter import *
import tkinter as dpc
import sqlite3
con = sqlite3.connect('datasv.db')
cur = con.cursor()
list = list(cur.execute("""select *
                    from DSSV"""))
print(list)
class xuat(dpc.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        dpc.Label(self, text="Danh sách sinh viên", font="30").grid(row=0, column=0, columnspan=3)
        dpc.Label(self, text="MSSV").grid(row=1, column=0)
        dpc.Label(self, text="Ten").grid(row=1, column=1)
        dpc.Label(self, text="Lop").grid(row=1, column=2)
class data(dpc.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        for i in range(len(list)):
            for j in range(len(list[0])):
                dc = StringVar()
                dc.set(list[i][j])
                dpc.Entry(self, textvariable=dc).grid(row=i, column=j)
def tang1():
    list[0] = ('1', '2', '2')
class buttons(dpc.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        dpc.Button(self, text="Find", command=tang1).grid(row=0, column=0)
        dpc.Button(self, text="Insert").grid(row=0, column=1)
        dpc.Button(self, text="Delete").grid(row=0, column=2)
        dpc.Button(self, text="Update").grid(row=0, column=3)


        

class Myapplication(dpc.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        xuat(self).pack()
        data(self).pack()
        buttons(self).pack()
        
        

        
if __name__=='__main__':
    app = Myapplication()
    app.mainloop()

