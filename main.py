from typing import List
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()
from langgraph.prebuilt import create_react_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
#from tavily import TavilyClient
from langchain_tavily import TavilySearch
#from langchain.agents import create_react_agent

class Source (BaseModel):
    """Schema for a source used by the agent"""
    url:str = Field (description="The url of the source")

class AgentResponse (BaseModel):
    """Schema for an agent reposnse with answer and sources"""
    answer:str = Field (description="The agent's answer to the query")
    sources: List[Source] = Field(default_factory=list, description="List of sources to generate the answer")

llm = ChatGroq(
    model="meta-llama/llama-4-scout-17b-16e-instruct"
)
tools = [TavilySearch ()]

agent = create_react_agent(
    model=llm,
    tools=tools,
    AgentResponse = AgentResponse
)

def main():
    result = agent.invoke(
        {
            "messages": [
                HumanMessage(
                    content="Weather in japan right now"
                )
            ]
        }
    )
    print(result)

if __name__ == "__main__":
    main()