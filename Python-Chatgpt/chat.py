import random
import openai
class ai:
    def __init__(self):
        self.x=0
        self.ans=""

    def get(self):
        print("Enter Number of Responses :")
        while(True):
            try:
                self.x=int(input())
                break
            except:
                print("Invalid Input Try Again")
        self.talk()
    def talk(self):
        print("Hello Lets Start talking")
        ctr=self.x
        while(ctr>0):
            q=str(input())
            self.ans=self.response(q)
            print(self.ans)
            ctr-=1
        print("Thats all in this session")

        
    def response(self,q : str)->str:
        openai.api_key="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"
        eng = "text-davinci-003"
        ques=q
        a = round(random.uniform(0.1,0.3),2)
        completion=openai.Completion.create(
            engine=eng,
            prompt=ques,
            max_tokens=100,
            temperature=a,
            n=1)
        reply=completion.choices[0].text
        return reply
ob1= ai()
ob1.get()