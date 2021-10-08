def price(a,b):
     #Hey please change password to ur sql password
     password='dpsgv'
     import mysql.connector as sqlob
     conn=sqlob.connect(user ='root' , host='localhost', database='albion',passwd=password)
     cursor=conn.cursor(buffered=True)
     cursor.execute("select {} from ench where tier={}".format(a,b))
     x=cursor.fetchall()
     return x[0]

def inp():
     while True:
          try:
               tier=int(input('choose tier [4-8]\n'))
               ench=str(input('choose from soul/rune/relic\n'))
               if((tier<9 and tier>3) and (ench=='soul' or ench=='rune' or ench=='relic')):
                    return tier,ench
               else:
                    raise NameError
               break
          except:
               print('! invalid input')
               print('choose from given Option')
def category():
     print("Choose the number to select from following category")
     print("1.1 handed weapon\n"
           "2.Weapon\n"
           "3.Armour\n"
           "4.Bag\n"
           "5.offhand,cape,boots,capes")
     while True:
          try:
               x=int(input(''))
               if(x>0 and x<6):
                    pass
               else:
                    raise
               break
          except:
               print('try again')
     required_number=[144,192,96,96,48]
     return required_number[x-1]

def history(x):
     #Hey please change password to ur sql password
     password='dpsgv'
     import mysql.connector as sqlob
     conn=sqlob.connect(host='localhost', user='root',passwd=password,database='albion')
     cursor=conn.cursor(buffered=True)
     for index in range(0,len(x)):
          while True:
               try:
                    item_name=str(input('please write the name of item whose price is {}'.format(x[index])))
                    if (item_name=='' or item_name[0].isdigit()):
                         raise NameError
                    else:
                         break
               except:
                    print('please write the correct name')
          q=('insert into history VALUES (%s,%s)')
          v=item_name,x[index]
          cursor.execute(q,v)
          conn.commit()
     print("thanks for the help have a nice day <3")
          


def main():
     item_list=[]
     cont='y'
     while cont.lower()=='y':     
          data=inp()
          unit_price=price(data[1],data[0])[0]
          number_of_units=category()
          total_price=unit_price*number_of_units
          choice=int(input("enter price of pre enchanted item"))
          choice2=int(input("enter price of post enchanted item"))
          print("unit price is {}".format(unit_price))
          print("total price of {} is {}".format(data[1],total_price))
          if((choice2-choice)>total_price):
               print("your profit will be",((choice2-choice)-total_price)*94.5/100)
          else:
               print("your loss will be",-((choice2-choice)-total_price)*94.5/100)
          item_list.append(choice)
          cont=str(input("Press 'y' key to use calc again and anyother key to exit "))
     feedback=str(input("hey would u like to help build data base \npress 'yes' to continue or press anyother key to exit:-"))
     if(feedback in 'yesYESyeahyo'):
          history(item_list)
     else:
          print("Thanks for coming have a nice day >.< <3")
     
main()

                        


