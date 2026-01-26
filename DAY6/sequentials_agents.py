# agent unutk menulis blog
# state -> menyimpan semua data (user input, ouput:research, output:writer, output:editor, output:final_article)
# -> AI Response = State['final_article']
# input -> research -> writer -> editor -> final_output (final_article)

from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, END, START
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, SystemMessage, BaseMessage
from typing import TypedDict, Annotated, List
from langgraph.checkpoint.memory import MemorySaver


# typeddict == dict sama tetapi 

class AgentState(TypedDict):
   # annotated berfungis sebagai deskripsi dari type data
   messages: Annotated[List[BaseMessage],add_messages]
   topic: str
   research_result: str
   draft_article: str
   final_article: str

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)

def research_agent(State: AgentState) -> AgentState:
    """Melakukan riset tentang topik yang diberikan"""
    print('research agent sudah melakukan tugasnya...')

    prompt= f""" Kamu adalah research assistent.
    Riset topik berikut dan berikan 3 -5 poin penting:{State['topic']}

    Format output:
    - Poin 1
    - Poin 2
    - Poin 3
    - dst...

    """
    response = llm.invoke([SystemMessage(content=prompt)])
    research = response.content

    return {
        'messages': [SystemMessage(content=f'Research: {research}')],
        'research_result': research
    }

def writer_agent(State: AgentState) -> AgentState:

    """Menulis draft  artikel berdasarkan hasil riset"""
    print('writer agent sudah melakukan tugasnya...')

    prompt = f"""Kamu adalah content writer profesional
    Topik: {State['topic']}
    
    Berdasarkan research berikut:
    {State['research_result']}
    
    Tulis draft artikel blog (300-400 kata) dengan struktur:
    - Judul menarik
    - Intro
    - Body (3 paragraf)
    - Kesimpulan
    
    """
    response = llm.invoke([SystemMessage(content=prompt)])
    draft = response.content

    return {
        'messages': [SystemMessage(content=f'Draft: {draft}')],
        'draft_article': draft
    }


def editor_agent(State: AgentState) -> AgentState:
    """Mengedit dan memperbaiki artikel"""
    print('editor agent sudah melakukan tugasnya...')

    prompt = f"""Kamu adalah seorang artikel editor profesional.

    Draft Artikel: 
    {State['draft_article']}
    
    Tugasmu:
    1. Perbaiki gramar dan typo
    2. Improve flow dan readability
    3. Pastikan artikel mudah dipahami
    4. Pertahankan gaya bahasa profesional
    5. Output final artikel yang sudah dipoles
    
    """
    response = llm.invoke([SystemMessage(content=prompt)])
    final = response.content

    return {
        'messages': [SystemMessage(content=f'Final: {final}')],
        'final_article': final
    }

def create_sequential_workflow():

    workflow = StateGraph(AgentState)
    workflow.add_node('research', research_agent)
    workflow.add_node('writer', writer_agent)
    workflow.add_node('editor', editor_agent)

    workflow.add_edge(START, 'research')
    workflow.add_edge('research', 'writer')
    workflow.add_edge('writer', 'editor')
    workflow.add_edge('editor', END)

    checkpointer = MemorySaver()

    return workflow.compile(checkpointer=checkpointer)


if __name__ == "__main__":
    print('sequential flow: Blog article generator')

    app = create_sequential_workflow()

    THREAD_ID = 'Ilmu mahal'

    user_input = input('\nMasukkan topik blog: ').strip()

    # inisialisasi state
    initial_state = {
        'messages': [HumanMessage(content=user_input)],
        'topic': user_input,
        'research_result': '',
        'draft_article': '',
        'final_article': ''
    }

    # invoke graph
    # menambahkan tred id ke memorynya
    app.invoke(initial_state, config ={'configurable': {'thread_id': THREAD_ID}})

    # ambil hasil akhir
    final_state = app.get_state(config ={'configurable': {'thread_id': THREAD_ID}})
    print(f"\n{final_state.values.get('final_article','Tidak ada hasil')}")

    while True:
        user_input = input("\nMasukkan topik blog: ").strip()
        
        delta ={
            'messages': [HumanMessage(content=user_input)],
            
        }

        app.invoke(delta, config ={'configurable': {'thread_id': THREAD_ID}})

        current = app.get_state(config ={'configurable': {'thread_id': THREAD_ID}})
        current_article = current.values.get('final_article','Tidak ada hasil')
        print(f"\n{current_article}")
        
        







    

    
    
    


