from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from config.llm_config import get_llm, get_autogen_config
from autogen import AssistantAgent
from sklearn.ensemble import IsolationForest
import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI

def create_fraud_agent():
    prompt = PromptTemplate(
        input_variables=["anomalies"],
        template="Based on the detected anomalies: {anomalies}, provide fraud alerts in the format: 'Fraud alerts: [Alert 1, Alert 2]' or 'Fraud alerts: None'."
    )
    chain = RunnableSequence(prompt | get_llm())
    agent = AssistantAgent(name="FraudAgent", llm_config=get_autogen_config())
    return chain, agent

def detect_anomalies(transactions_df):
    model = IsolationForest(contamination=0.1, random_state=42)
    transactions_df["anomaly"] = model.fit_predict(transactions_df[["amount"]])
    anomalies = transactions_df[transactions_df["anomaly"] == -1]
    return anomalies["description"].tolist() if not anomalies.empty else "None"
