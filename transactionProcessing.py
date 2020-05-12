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
    
    cur.execute("INSERT INTO Student( name, subject, marks) VALUES ('Anvi134','Python',45)")
    #raise InvalidException #throw
    cur.execute("INSERT INTO Student( name, subject, marks) VALUES ('Saransh1234','Python',45)")
    mydb.commit()
except:
    print('Exception Raised')
    mydb.rollback()
finally:
    mydb.close() # No