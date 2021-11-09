class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None


    def add(self,data):
        new_node=node(data)
        new_node.next=self.head
        self.head=new_node


    def push(self,data):
        new_node=node(data)
        if self.head == None:
            self.head=new_node
        else:
            tmp = self.head
            while(tmp.next):
                tmp=tmp.next
            tmp.next=new_node
            new_node.next=None


    def place(self,data,index=0):
        tmp=self.head
        new_node=node(data)
        if(index==0 or index==1):
            new_node.next=tmp
            self.head=new_node
            return 
        for x in range(index-2):
            tmp=tmp.next
            if(tmp==None):
                print("position not in Linked-List")
                return
            elif(tmp.next==None):
                self.push(data)
                return
        tmp2=tmp.next.next
        tmp.next=None
        tmp.next=new_node
        new_node.next=tmp2

    def delete(self,pos=0):
        tmp=self.head
        if(self.head==None):
            print("List is empty, postion not found")
            return
        if(pos==0):
            self.head=tmp.next
            return
        for x in range(pos-1):
            if(tmp.next==None):
                print("KeyError Position greater then list")
                return
            tmp=tmp.next
        if (tmp==None or tmp.next ==None):
            print("KeyError Position greater then list")
            return
        tmp2=tmp.next.next
        tmp.next = None
        tmp.next=tmp2

    def dellist(self):
        self.head=None

    def reverse(self):
        tmp=None
        curr=self.head
        while self.head is not None:
            next=curr.next
            curr.next=tmp
            tmp=curr
            curr=next
        self.head=tmp



    def printList(self):
        tmp=self.head
        while tmp != None:
            print(tmp.data,end=" ")
            if(tmp.next!=None):
                print("->",end=" ")
            tmp=tmp.next
        print()


def generator(ar:str,N:int,llist):
    elem=[int(x) for x in ar.strip().split()]
    for x in range(N):
        llist.add(elem[x])
    llist.printList()
def deletion(llist):
    pos=int(input("enter index of number to delete\n"))
    llist.delete(pos)
    llist.printList()

    
def main():
    llist=LinkedList()
    len_ar=int(input("enter the number of elements=>  "))
    ar_str=str(input("enter {} space separated integers=> ".format(len_ar)))
    generator(ar_str,len_ar,llist)
    token=input("do you want to delete a element  ")
    if (token=="y"):
        deletion(llist)
    else:
        print("Bbye")    
#driver code
main()


