def Push(stack):
     x='y'
     while x=='y':
          val=input('enter data')
          stack.append(val)
          top=len(stack)-1
          x=input('do you want to add more in the stack')
          if(x=='no'):
               break
def underflow(stack):
     if(len(stack)<=0):
          
          return False
               
     else:
          return True
def POP(stack):
     if(underflow(stack)):
          obj=stack.pop()
          top=len(stack)-1
          return obj
     else:
          return "stack is empty"
def display(stack):
     if(underflow(stack)):
          top=len(stack)-1
          while(top>=0):
               print(stack[top])
               top-=1
     else:
          print('stack is empty')
print('Welcome to stack')
print("1)Push\n"
      "2)Pop\n"
      "3)Display\n"
      "4)Exit\n"
      )

init=True
stack=[]
top=-1
while init:
     while True:
          try:
               inp=int(input('enter option=>'))
               break
          except :
               print("ENTER A NUMBER >.<")
     if(inp==1):
          Push(stack)
     elif(inp==2):
          print(POP(stack))
     elif(inp==3):
          display(stack)
     elif(inp==4):
          print('Thanks for coming have a nice day!')
          init=False
          
     else:
          print('wrong input try again')
          inp=int(input('enter option=>'))
