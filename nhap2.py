import sqlite3
from tkinter import *
import tkinter as tk
con = sqlite3.connect('datasv.db')
cur = con.cursor()
list = list(cur.execute("""SELECT *
                            FROM DSSV"""))
print(list)

for i in len(list):
    for j in len(list[0]):
        print(i+j)
