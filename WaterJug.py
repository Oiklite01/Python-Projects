#Lab Experiment 6, Water Jug problem
def pour(toJugCap,fromJugCap,d,arr):
    toJug=0
    fromJug=fromJugCap
    arr=[[0,0],[fromJug,toJug]]
    while ((fromJug  is not d) and (toJug is not d)):
        temp = min(fromJug, toJugCap-toJug)
 
        toJug = toJug + temp
        fromJug = fromJug - temp
        arr.append([fromJug,toJug])
        if ((fromJug == d) or (toJug == d)):
            break
 
        if fromJug == 0:
            fromJug = fromJugCap
            arr.append([fromJug,toJug])
        if toJug == toJugCap:
            toJug = 0
            arr.append([fromJug,toJug])
    arr.append([fromJug,toJug])

    for x in arr:
        print(x,end=" ")
    

def gcd(m,n) ->  int:
    a=n
    b=m
    while(b%a!=0):
        temp=a
        a=b%a
        b=temp
    return a

m=int(input("Enter capacity of Big jug: "))
n=int(input("Enter capacity of Small jug: "))
target=int(input("Enter Target: "))
if((target%gcd(m,n)) != 0):
    print(-1)
else:
    pour(m,n,target,[])


