from tkinter import *
from tkinter import messagebox
import tkinter as tk
import sqlite3
#connect database



# create gui
window = Tk()
window.title("NHOM 4 - TKCSDL")
window.geometry("1024x576")
window.configure(background="white")
# 
id = StringVar()
name = StringVar()
clas = StringVar()
# creaty empty list StringVar
list = []
for i in range(20):
    tam = []
    for j in range(3):
        v = StringVar()
        tam.append(v)
    list.append(tam)

size = (150, 210, 150)
for i in range(20):
        loc = 0
        for j in range(3):
            qlb = Label(window, textvariable=list[i][j], relief=RAISED, font='Arial 14', bg="white")
            qlb.place(width=size[j],height=30,x=loc+160,y=(8+i)*30)
            loc=loc+size[j]

Label(text="ID", font="20").place(x=100, y=80)
Entry(textvariable=id, width=20, border='2', font="20").place(x=160, y=80)

Label(text="Name", font="20").place(x=100, y=110)
Entry(textvariable=name, width=20, border='2', font="20").place(x=160, y=110)

Label(text="Class", font="20").place(x=100, y=140)
Entry(textvariable=clas, width=20, border='2', font="20").place(x=160, y=140)
def find():
    con = sqlite3.connect('datasv.db')
    cur = con.cursor()


    cur.execute("""SELECT * FROM DSSV""")
    tam = cur.fetchall()
    lst = []
    for i in tam:
        if id.get()=="" or i[0]==id.get():
            if name.get()=="" or i[1]==name.get():
                if clas.get()=="" or i[2]==clas.get():
                    lst.append(i)
    print(lst)
    for i in range(20):
        for j in range(3):
            if i<len(lst): 
                list[i][j].set(lst[i][j])
            else:
                list[i][j].set("")
    cur.close()



def reset():
    con = sqlite3.connect('datasv.db')
    cur = con.cursor()
    cur.execute("""select * from DSSV""")
    lst = cur.fetchall()
    id.set("")
    name.set("")
    clas.set("")
    
    
    for i in range(20):
        for j in range(3):
            if i<len(lst): 
                list[i][j].set(lst[i][j])
            else:
                list[i][j].set("")
    cur.close()
    con.close()
def insert():
    con = sqlite3.connect('datasv.db')
    cur = con.cursor()
    try:
        cur.execute("INSERT INTO DSSV(ID, NAME, CLASS) VALUES(?, ?, ?)", (id.get(), name.get(), clas.get()) )
        con.commit()
    except sqlite3.Error as e:
        messagebox.showinfo("Error", e)
    cur.close()
    con.close()
    reset()
    

Button(text="Find", width="15", command=find).place(x=500, y=50)
Button(text="Insert", width="15", command=insert).place(x=500, y=80)
Button(text="Delete", width="15").place(x=500, y=110)
Button(text="Update", width="15").place(x=500, y=140)
Button(text="Reset", width="15", command=reset).place(x=500, y=170)
reset()



lb = ['StudentID','StudentName','ClassID']

loc = 0
for i in range(len(lb)):
    qlb = Label(window, text = lb[i], font='Arial 15 bold', relief='solid', border='2')
    qlb.place(width=size[i], height=30, x=loc+160, y=210)
    loc=loc+size[i]

window.mainloop()