from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_AI_API_KEY")
)

# client.chat.completions.create() pasti memakai ini
response= client.chat.completions.create(
    model='gpt-4o-mini',
    messages=[
        {'role':'system','content':'You are a helpful assistant.'},
        {'role':'user','content':'Jelaskan kepada saya tentang quantum computing.'},
    ]
)

print(response.choices[0].message.content)