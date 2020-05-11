import mysql.connector

mydb  = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '',
    database= 'PythonPractice'
)
cur = mydb.cursor()
cur.execute("INSERT INTO `Student`( `name`, `subject`, `marks`) VALUES ('Divyansh','Python',45)")
cur.execute("INSERT INTO `Student`( `name`, `subject`, `marks`) VALUES ('Anvi','Python',55)")
cur.execute("INSERT INTO `Student`( `name`, `subject`, `marks`) VALUES ('Sarthak','Python',65)")
mydb.commit()
mydb.close()