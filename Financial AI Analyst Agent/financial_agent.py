from phi.agent import agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai

import os
from dotenv import load_dotenv
load_dotenv()
openai.api_key=os.getenv("OPENAI_API_KEY")




## Web Search Agent
web_search_agent = agent(
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

multi_Ai_agent=Agent(
    model=Groq(id="llama-3.1-70b-versatile"),
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources","Use Table to display the data"],
    show_tool_calls=True,
    markdown=True,

)

multi_Ai_agent.print_response("Summerize analyst Reccomendation and share the latest news for NVDA", stream=True)








