from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_AI_API_KEY")
)

SYSTEM_PROMPT='you are a helpful assistant.'
MAX_HISTORY=12*2+1

history = [
    {'role':'system','content':SYSTEM_PROMPT},
]

while True:
    user_chat = input('You: ')
    
    #/exit seesai looping
    if user_chat =='/exit':
        break
    
    history.append({'role':'user','content':user_chat})
    
    # client.chat.completions.create() pasti memakai ini
    response= client.chat.completions.create(
        model='gpt-4o-mini',
        messages=history
    )
    
    history.append({'role':'assistant','content':response.choices[0].message.content})
    
    # if len(history)>MAX_HISTORY:
    #     # summarize
    #     response= client.chat.completions.create(
    #         model='gpt-4o-mini',
    #         messages=[] 
    #         # tolong summary history ini
    #     )
    #     new_history=history[0]
    #     history=new_history

    print(f'AI:{response.choices[0].message.content}')