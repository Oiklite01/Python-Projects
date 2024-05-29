def show_all():
     import mysql.connector as mysqlob
     myconn=mysqlob.connect(host='localhost',user='root',passwd='dpsgv',database='csproject')
     cursor=myconn.cursor()
     a='computer'
     cursor.execute("select question from %s"%(a,))
     x=cursor.fetchall()
     cursor.execute('select question from {table}'.format(table=a))
     y=cursor.fetchone()
     for record in range (0,len(x)):
          print(record+1,*x[record])
          
     print("fetch one command :-",*y)

show_all()

     
