from dotenv import load_dotenv
load_dotenv ()
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from tavily import TavilyClient


tavily = TavilyClient ()
@tool
def search (query:str) -> str:
   """
   Tool that searches over the internet
   Args:
   query: The query to search for
   Returns:
       The search result
   """
   print (f"Searching for {query}")
   return str (tavily.search (query = query))

llm = ChatGroq (model="llama-3.3-70b-versatile")
tools = [search]
agent = create_react_agent (model = llm, tools = tools)

def main():
    print("Hello from langchain-course!")
    result = agent.invoke ({"messages":[HumanMessage(content = "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and their details")]})
    print (result)
if __name__ == "__main__":
    main()
