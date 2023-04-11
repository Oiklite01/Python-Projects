import random
import openai
openai.api_key="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"
eng = "text-davinci-003"
f=open("influence.txt","r")
ques=f.read()+"what is an orange"
a = 0.1#round(random.uniform(0.1,0.9),2)
completion=openai.Completion.create(
    engine=eng,
    prompt=ques,
    max_tokens=100,
    temperature=a,
    n=1
)
response=completion.choices[0].text
print(response)




