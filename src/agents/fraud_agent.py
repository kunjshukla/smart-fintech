from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from config.llm_config import get_llm, get_autogen_config
from autogen import AssistantAgent
from sklearn.ensemble import IsolationForest
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI

def create_fraud_agent():
    prompt = PromptTemplate(
        input_variables=["transactions"],
        template="""Analyze these transactions for potential fraud:
        {transactions}
        
        Return any suspicious transactions in the format:
        - [Amount]: [Reason for suspicion]"""
    )
    llm = get_llm()
    return prompt | llm