from agents.budget_agent import create_budget_agent
from agents.investment_agent import create_investment_agent
from agents.fraud_agent import create_fraud_agent
from agents.report_agent import create_report_agent


def run_financial_analysis(transactions=None, income=0, expenses=0, risk_profile="moderate"):
    print(f"\n[DEBUG] Starting financial analysis with risk_profile: {risk_profile}")

    try:
        # Initialize agents
        budget_agent = create_budget_agent()
        investment_agent = create_investment_agent()
        fraud_agent = create_fraud_agent()
        report_agent = create_report_agent()


        def extract_content(response):
            """Extract content from LLM response, handling different response types."""
            if hasattr(response, 'content'):
                return response.content
            elif isinstance(response, dict) and 'content' in response:
                return response['content']
            return str(response)
        
        # Calculate total from transactions if provided
        if transactions:
            expenses = sum(tx.get('amount', 0) for tx in transactions)
        
        # Get budget advice
        budget_summary = budget_agent.invoke({"income": income, "expenses": expenses})
        
        # Calculate savings
        savings = income - expenses
        investment_advice = investment_agent.invoke({"savings": savings, "risk_profile": risk_profile})
        fraud_alerts = fraud_agent.invoke({"transactions":transactions})
        report_response = report_agent.invoke({
            "budget_advice": budget_summary,
            "investment_advice": investment_advice,
            "fraud_alert": fraud_alerts
        })   

        # Extract content if it's an AIMessage object
        report = extract_content(report_response)
        # Generate report
        # report = f"""Financial Analysis Report
        # ====================  
        # Income: ${income}
        # Expenses: ${expenses}
        # Savings: ${savings}

        #  Budget Summary:
        # {budget_summary}

        # Investment Advice:
        # {investment_advice}"""
        
        return {
            "budget_summary": budget_summary,
            "investment_advice": investment_advice,
            "fraud_alerts": fraud_alerts,
            "financial_report": report
        }

    except Exception as e:
        return {"error": str(e)}