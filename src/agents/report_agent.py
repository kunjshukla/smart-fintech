from langchain.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from autogen import AssistantAgent
from config.llm_config import get_llm, get_autogen_config

def create_report_agent():
    prompt = PromptTemplate(
        input_variables=["budget_advice", "investment_advice", "fraud_alert"],
        template="""Generate a financial report based on the following data:
- Budget Advice: {budget_advice}
- Investment Advice: {investment_advice}
- Fraud Alerts: {fraud_alert}

Format the report as:
Financial Report:
- Savings Plan: [summary]
- Investment Options: [summary]
- Security Alerts: [summary]
Return only the report text, no additional formatting or metadata."""

)
    llm = get_llm()
    return prompt | llm