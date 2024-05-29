def free(l,s):
     print(l)
     while (len(l)>1):
          tmp=[]
          end=len(l)-(len(l)%s)
          tmp.extend(l[end:])
          l=l[:end]
          for i in range(s-1,end,s):
               l[i]=-1
          for e in l:
               if(e<0):
                    l.remove(e)
          tmp.extend(l)
          l=tmp
          print(l)
     else:
          return l[0]
a=int(input("enter number of prisoner"))
b=int(input("enter number of steps"))
initial=[x for x in range(a)]
free(initial,b)



