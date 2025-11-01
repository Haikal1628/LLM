from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPEN_AI_API_KEY")
)

try:
    models= client.models.list()
    print('sukses')
    print(f'Allmodels: {models.data}')

except Exception as e:
    print(f'Error: {e}')