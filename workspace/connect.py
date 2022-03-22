import pymysql

connection = pymysql.connect(host='localhost',
                             database='EXAMPLE',
                             user='root',
                             password='5985593')

mycursor = connection.cursor()
# insert_commit = "INSERT INTO city VALUES(%s, %s)"
# data = ('103', 'hisnchu')
# mycursor.execute(insert_commit, data)
# connection.commit()
mycursor.execute("SELECT * FROM EMP")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
