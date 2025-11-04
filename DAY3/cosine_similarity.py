from openai import OpenAI
import os
from dotenv import load_dotenv
import numpy as np
load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

# text='gue ganteng banget sih'
def get_embeddings(text):
    response = client.embeddings.create(
        model='text-embedding-3-small',
        input=[text]
    )

    embedding_data = response.data[0].embedding
    
    return embedding_data


# cosine similarity = dot(A,B) / (||A|| * ||B||)
# vektor awalnya list, ubah ke numpy array untuk mempermudah operasi matematika
# magnitude = panjang vektor = sqrt(x1^2 + x2^2 + ... + xn^2)
def cosine_similarity(vector1,vektor2):
    vector1 = np.array(vector1)
    vektor2 = np.array(vektor2)
    
    dot_product = np.dot(vector1, vektor2)
    magnitude1= np.linalg.norm(vector1)
    magnitude2= np.linalg.norm(vektor2)
    
    return dot_product / (magnitude1 * magnitude2)

text1='aku baik banget'
text2='au jahat banget'

emb1= get_embeddings(text1)
emb2= get_embeddings(text2)
similarity= cosine_similarity(emb1,emb2)

# hasilnya harus mendekati 1 karena teksnya mirip
print(f'Text 1: {text1}')
print(f'Text 2: {text2}')
print(f'Cosine Similarity: {similarity}')
    

