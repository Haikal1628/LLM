from openai import OpenAI
import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

prompt = 'gambar garuda'# -> improve prompt

# client.images.generate
response = client.images.generate(
    model='dall-e-3',
    prompt=prompt,
    size='1024x1024', # 1:1
    quality='hd',
    n=1 #jumlah gamabar yang di generate
)


# client.images.generate(
#   model="gpt-image-1",
#   prompt=prompt,
#   background="auto",
#   n=1,
#   quality="high",
#   size="1024x1024",
#   output_format="png",
#   moderation="auto",
# )

# melihat URL
image_url = response.data[0].url
print(f'URL: {image_url}')

image_data = requests.get(image_url).content
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
file_name = f'gambar_{timestamp}.png'
with open(file_name, 'wb') as f:
    f.write(image_data)