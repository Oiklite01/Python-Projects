class emp:
     def __init__(self,a,b,**kwargs):
          self.first_name=a
          self.last_name=b
          for k,v in kwargs.items():
               setattr(self,k,v)
Rohan=emp("Rohan","foo",age=12)
print(Rohan.age)
