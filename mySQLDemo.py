import mysql.connector

mydb  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database= 'PythonPractice'
)

fp = open('StudentTableRecord.csv','w')

cur = mydb.cursor()
cur.execute('select * from Student')


for x in cur:
    print(','.join(list(map(str,x))),file=fp)

fp.close()
mydb.close()