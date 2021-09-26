import sqlite3
con = sqlite3.connect('datasv.db')
cur = con.cursor()
cur.execute("""INSERT INTO DSSV VALUES ('S02', 'DF', '55') """)
"""con.commit()
result = cur.execute("""select *
                        from DSSV """)
for i in result:
    print(i)"""