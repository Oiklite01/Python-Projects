import random

def shuffle(word):
    a=''
    b=list(word)
    for _ in range(20):
        temp=random.randint(0,len(b)-1)
        temp2=random.randint(0,len(b)-1)
        b[temp2],b[temp]=b[temp],b[temp2]
    for x in b[::-1]:
        a+=x
    return a

def choose():
    rand=random.randint(0,len(word_list))
    ans=word_list[rand]
    ques=shuffle(ans)
    return [ques,ans]

def main():
    print("This is Jumbled Word Game")
    print("You have 5 tries to Guess the jumbled words")
    c=str(input("press y to start\t"))
    while(c=='y'):
        print("___________________________________________________________")
        t=1
        ques,ans=choose()
        print(f"Try to make the correct word from {list(ques)}")
        while(t<6):
            temp=str(input(f"{t}."))
            if(temp==ans):
                break
            else:
                t+=1
        if(t<6):
            print("You Won!!!")
        else:
            print(f"You Lost =( \nThe correct word was {ans} ")
        
        
        c=str(input("Do you want to replay (y/n) \t"))
    print("Thanks for Playing")

#driver code
file=open('wordlist.txt','r')
word_list=file.read()
word_list=word_list.split('\n')
main()

    
