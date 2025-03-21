import openai 
from phi.agent import agent
import phi.api
from phi.model.openai import OpenAIChat
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
from phi.model.groq import Groq


import os
import phi 
from phi.playground import Playground, serve_playground_app
#Load environment variables from .env file
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

## Web Search Agent
web_search_agent = Agent(
    name = "web search Agent",
    role = "Serach the web for the information",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools = [DuckDuckGo()],
    instructions = ["Always includes sources"],
    show_tools_calls = True,
    markdown = True,

)

## Financial Agent
finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True, historical_prices=True, technical_indicators=True)
        ],
    show_tool_calls=True, 
    markdown=True,
    instructions=["Use Tables to display the data"],    

)

app=Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)
    
