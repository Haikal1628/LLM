from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
# perlu system prompt, user prompt, dan message history
from langchain_core.prompts import ChatPromptTemplate

# messaages = []

# chain = input -> llm ->output
# chain = history massage -> llm -> output

# prompt
# formatnya adalah list of tuple
SYSTEM_PROMPT = """
Kamu adalah asisten yang membantu
"""

prompt = ChatPromptTemplate([
    ("system", SYSTEM_PROMPT), # ini adalah system prompt
    ("human", "{input}") # ini adalah user prompt
])


llm = ChatOpenAI(
    model='gpt-4o-mini',
)

chain = prompt | llm # prompt -> llm

# Chat looping
while True:
    user_text = input('\nYou: ').strip()
    
    ai_message = chain.invoke({'input':user_text})
    print(f'AI: {ai_message.content}')
