import logging
import warnings
import pandas as pd
from core.advisor import run_financial_analysis
from app_parser import parse_transactions

# Configure logging
logging.basicConfig(level=logging.INFO)
warnings.filterwarnings("ignore", category=DeprecationWarning, module="paramiko")
logging.getLogger('grpc').setLevel(logging.WARNING)

if __name__ == "__main__":
    # Sample risk profile
    risk_profile = "moderate"

    # Parse transactions from CSV
    transactions = parse_transactions("data/transactions.csv")
    
    # If no transactions found in CSV, use sample data
    if not transactions:
        print("No transactions found in data/transactions.csv. Using sample transactions.")
        transactions = [
            {"amount": 500, "description": "Vendor A"},
            {"amount": 1000, "description": "Vendor B (flagged)"}
        ]
    else:
        print(f"Loaded {len(transactions)} transactions from CSV")

    # Run financial analysis
    result = run_financial_analysis(
        transactions=transactions,
        risk_profile=risk_profile
    )
    
    # Display results
    print("\nBackend Test Results (Using CSV Transactions):")
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("\nBudget Advice:")
        print("-------------")
        print(result["budget_summary"])
        
        print("\nInvestment Advice:")
        print("-----------------")
        print(result["investment_advice"])
        
        print("\nFraud Alerts:")
        print("------------")
        print(result["fraud_alerts"])
        
        print("\nFinancial Report:")
        print("---------------")
        print(result["financial_report"])