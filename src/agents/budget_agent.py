from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config.llm_config import get_llm

def create_budget_agent():
    prompt = PromptTemplate(
        input_variables=["income", "expenses"],
        template="""Given an income of ${income} and expenses of ${expenses}, calculate the savings and provide a brief budget summary.
        Format your response as: 'Savings: $X. [Brief summary]'"""
    )
    llm = get_llm()
    return prompt | llm  # Using the newer pipe syntax

def process_transactions(transactions):
    # Simple transaction processing - sum amounts
    total = sum(tx.get('amount', 0) for tx in transactions)
    return total