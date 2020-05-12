import sqlite3

mydb = sqlite3.connect('new_db1.db')

cur = mydb.cursor()
cur.execute('select * from student')
#cur.execute('create table student (name text,class text,marks real)')
#cur.execute('insert into student values ("Divyansh","Python",45) ')
#cur.execute('insert into student values ("Anvi","Python",55) ')
#cur.execute('insert into student values ("Saransh","Python",65) ')
#mydb.commit()
for x in cur:
    print(x)

mydb.close()