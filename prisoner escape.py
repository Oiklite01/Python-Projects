def free(n,s):
     i=0
     l=[x for x in range(n)]
     while (len(l)>1):
          tmp=[]
          if(len(l)>=s):
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
          else:
               for x in range(s):
                    i+=1
                    if(i>=len(l)):
                         i=0
               l.remove(l[i])
               i=i-1
     return l[0]

#a=int(input("enter number of prisoner"))
#b=int(input("enter number of steps"))
a=1
b=2
while(True):
     a+=1
     print(a,"prisoners\n",free(a,b),"will be free")


