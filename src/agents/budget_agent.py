from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from autogen import AssistantAgent
from config.llm_config import get_llm, get_autogen_config
import pandas as pd

def process_transactions(transactions_df, chain):
    try:
        # Calculate income and expenses
        income = transactions_df[transactions_df["amount"] > 0]["amount"].sum()
        expenses = abs(transactions_df[transactions_df["amount"] < 0]["amount"].sum())
        
        # Get the response from the LLM
        response = chain.invoke({"transactions": transactions_df.to_string()})
        
        # Extract the content if it's an AIMessage
        if hasattr(response, 'content'):
            return str(response.content)
        return str(response)
    except Exception as e:
        return f"Error processing transactions: {str(e)}"

def create_budget_agent():
    prompt = PromptTemplate(
        input_variables=["transactions"],
        template="Analyze these transactions: {transactions}. Provide a budget summary."
    )
    llm = get_llm()
    chain = prompt | llm
    agent = AssistantAgent(
        name="BudgetAgent",
        llm_config=get_autogen_config()
    )
    return chain, agent