#FetchOne, Fetchmany and Fetchall
import mysql.connector

class InvalidException(Exception):
    pass

try:
    mydb = mysql.connector.connect(
        host='localhost',
        database='pythonpractice',
        passwd='',user='root'
    )
    cur = mydb.cursor()
    cur.execute('select * from student')
    result = cur.fetchmany(5)
    for x in result:
       print (x)
    
    #print(result)
  
except:
    print('Exception Raised')
