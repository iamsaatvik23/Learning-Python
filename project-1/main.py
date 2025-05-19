


if __name__ == "__main__":
    main()


from langchain_core.messages import HumanMessage #allows us to build ai applications
from langchain_openai import ChatOpenAI #allows us use apenai
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent #allows us to create ai agents
from dotenv import load_dotenv #allows us load environment variable files into python script

load_dotenv()

def main():
    model = ChatOpenAI(temperature=0) # higher the temp. more randomness
    tools=[]
    agent_executer= create_react_agent(model,tools)
    
