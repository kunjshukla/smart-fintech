from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from autogen import AssistantAgent
from config.llm_config import get_llm, get_autogen_config

def create_investment_agent():
    prompt = PromptTemplate(
        input_variables=["savings", "risk_profile"],
        template="Based on monthly savings of ${savings} and risk profile '{risk_profile}', recommend investment options in the format: 'Recommended investments: [Option 1, Option 2]'."
    )
    chain = RunnableSequence(prompt | get_llm())
    agent = AssistantAgent(name="InvestmentAgent", llm_config=get_autogen_config())
    return chain, agent