from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from config.llm_config import get_llm

def create_investment_agent():
    prompt = PromptTemplate(
        input_variables=["savings", "risk_profile"],
        template="""Given ${savings} in savings and a {risk_profile} risk profile, 
        recommend investment options. Format your response as a list starting with 'Recommended investments:'.
        Include at least 3 options with brief descriptions.""",
    )
    llm = get_llm()
    return prompt | llm