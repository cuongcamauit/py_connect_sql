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

def taochuoi(id, name, clas):
    s = ""
    if id.get()!="":
        s = s + " ID='%s'" %(id.get())
    if name.get()!="":
        if s!="":
            s = s + " AND NAME='%s'" %(name.get())
        else:
            s = s + " NAME='%s'" %(name.get())
    if clas.get()!="":
        if s!="":
            s = s + " AND CLASS='%s'" %(clas.get())
        else:
            s = s + " CLASS='%s'" %(clas.get())
    return s
def find():
    con = sqlite3.connect('datasv.db')
    cur = con.cursor()


    try:
        cur.execute("SELECT * FROM DSSV WHERE" + taochuoi(id, name, clas))
    except sqlite3.Error as e:
        messagebox.showerror("Error", e)
    lst = cur.fetchall()
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
def delete():
    con = sqlite3.connect('datasv.db')
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM DSSV WHERE " + taochuoi(id, name, clas))
        con.commit()
    except sqlite3.Error as e:
        messagebox.showinfo("Error", e)
    cur.close()
    con.close()
    reset()
new_id = StringVar()
new_name = StringVar()
new_clas = StringVar()

def update_thiet_ne():
    con = sqlite3.connect('datasv.db')
    cur = con.cursor()
    print("UPDATE DSSV SET" + taochuoi(new_id, new_name, new_clas) + " WHERE" + taochuoi(id, name, clas))
    cur.execute("UPDATE DSSV SET" + taochuoi(new_id, new_name, new_clas) + " WHERE" + taochuoi(id, name, clas))
    con.commit()
    
    cur.close()
    con.close()
    reset()
def update():
    win = Tk()
    Label(win, text="newID").grid(row=0, column=0)
    Label(win, text="newNAME").grid(row=1, column=0)
    Label(win, text="newCLASS").grid(row=2, column=0)
    Entry(win, textvariable=new_id).grid(row=0, column=1)
    Entry(win, textvariable=new_name).grid(row=1, column=1)
    Entry(win, textvariable=new_clas).grid(row=2, column=1)
    Button(win, text="OK", command=update_thiet_ne).grid(row=3, column=0)
    Button(win, text="Cancel", command=win.destroy).grid(row=3, column=1)
    win.mainloop()



Button(text="Find", width="15", command=find).place(x=500, y=50)
Button(text="Insert", width="15", command=insert).place(x=500, y=80)
Button(text="Delete", width="15", command=delete).place(x=500, y=110)
Button(text="Update", width="15", command=update).place(x=500, y=140)
Button(text="Reset", width="15", command=reset).place(x=500, y=170)
reset()



lb = ['StudentID','StudentName','ClassID']

loc = 0
for i in range(len(lb)):
    qlb = Label(window, text = lb[i], font='Arial 15 bold', relief='solid', border='2')
    qlb.place(width=size[i], height=30, x=loc+160, y=210)
    loc=loc+size[i]

window.mainloop()