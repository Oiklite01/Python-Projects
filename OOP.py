import pickle
class quests:
     def __init__(self,name,what_to_do,description,price):
          self.name=name
          self.motive=what_to_do
          self.desc=description
          self.reward=price
          self.list=[self.name,self.motive,self.desc,self.reward]

def gen():
     final=[]
     inp=int(input('number of quests to add'))
     for num in range(0,inp):
          n=str(input('Name=>'))
          m=str(input('Motive=>'))
          d=str(input('description=>'))
          p=str(input('Rewards=>'))
          x=quests(n,m,d,p)
          final.append(x.list)
     return final

def wrtr():
     a=open('Quests.dat','wb+')
     pickle.dump(gen(),a)
     a.close()
def new_quest(data):
     for x in (gen()):
          data.append(x)
     a=open('Quests.dat','wb+')
     pickle.dump(data,a)
     a.close
def data():
     b=open('Quests.dat','rb')
     c=pickle.load(b)
     b.close()
     return c
new_quest(data())
print(data())







'''n=str(input('name'))
for x in data:
     if(n==x[0]):
          c+=1
          print(x)
          break
     else:
          pass
if(c==0):
     print("quest  not found")'''
     










