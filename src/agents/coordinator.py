from autogen import AssistantAgent, UserProxyAgent
from .budget_agent import create_budget_agent
from .investment_agent import create_investment_agent
from .fraud_agent import create_fraud_agent

def create_coordinator():
    user_proxy = UserProxyAgent(
        name="User",
        # Remove the unsupported parameter
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE")
    )
    coordinator = AssistantAgent(
        name="Coordinator",
        system_message="You are a coordinator for a financial advisory system. Route tasks to the appropriate agent based on user input."
    )
    budget_chain, budget_agent = create_budget_agent()
    investment_chain, investment_agent = create_investment_agent()
    fraud_chain, fraud_agent = create_fraud_agent()
    return coordinator, user_proxy, {
        "budget": (budget_chain, budget_agent),
        "investment": (investment_chain, investment_agent),
        "fraud": (fraud_chain, fraud_agent)
    }