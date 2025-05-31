from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from autogen import AssistantAgent
from config.llm_config import get_llm, get_autogen_config

def create_report_agent():
    prompt = PromptTemplate(
        input_variables=["budget_advice", "investment_advice", "fraud_alert"],
        template="Generate a financial report based on the following data:\n- Budget Advice: {budget_advice}\n- Investment Advice: {investment_advice}\n- Fraud Alerts: {fraud_alert}\nFormat the report as: 'Financial Report:\n- Savings Plan: ...\n- Investment Options: ...\n- Security Alerts: ...'"
    )
    chain = RunnableSequence(prompt | get_llm())
    agent = AssistantAgent(name="ReportAgent", llm_config=get_autogen_config())
    return chain, agent