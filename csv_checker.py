import CSV
a=['name','rollnumber','exam']
b=[['abc',12,'jee'],
     ['xyz',13,'neet'],
      ['qwe' , 17 ,'jee' ]]
with open('test.csv','w') as f :
     cx = CSV.writer(f)
     cx.writerow(a)
     cx.writerows(b)
n=input("start?y/n  ")
s=input("read/write/search  ")
while(n=='y'):
     if(s=="read"):
          with open('test.csv','r') as f :
               demo = csv.reader(f)
               for row in demo:
                    print(row)
          n=input("you wish to continue??y/n  ")
          s=input("read/write/search  ")
     elif (s=="write"):
          with open('test.csv','a') as f :
               new=eval(input("write what you want..   "))
               
          n=input("you wish to continue??y/n  ")
          s=input("read/write/search  ")
     else:
          kl=int(input('number of row you want to see  '))
          with open('test.csv','r') as f :
               dx = csv.reader(f)
               rows= list(dx)
               print(rows[kl-1])
               
          n=input("you wish to continue?y/n?  ")
          s=input("read/write/search  ")


