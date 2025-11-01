from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_AI_API_KEY")
)


while True:
    user_chat = input('You: ')
    
    #/exit seesai looping
    if user_chat =='/exit':
        break
    
    # client.chat.completions.create() pasti memakai ini
    response= client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[
            {'role':'system','content':'You are a helpful assistant.'},
            {'role':'user','content':user_chat},
        ]
    )

    print(f'AI:{response.choices[0].message.content}')