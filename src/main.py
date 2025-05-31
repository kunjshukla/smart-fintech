import logging
import warnings
import pandas as pd
warnings.filterwarnings("ignore", category=DeprecationWarning, module="paramiko")

# Suppress gRPC logs
logging.getLogger('grpc').setLevel(logging.WARNING)

from core.advisor import run_financial_analysis

if __name__ == "__main__":
    # Create a DataFrame from the transactions
    transactions_df = pd.DataFrame([
        {"amount": 500, "description": "Vendor A"},
        {"amount": 1000, "description": "Vendor B (flagged)"}
    ])
    
    # Run the analysis with the new function signature
    result = run_financial_analysis(
        transactions=transactions_df.to_dict('records'),  # Convert DataFrame to list of dicts
        risk_profile="moderate"
    )
    
    print("Backend Test Results:")
    if "error" in result:
        print(result["error"])
    else:
        print("Budget Advice:", result["budget_summary"])
        print("Investment Advice:", result["investment_advice"])
        print("Fraud Alerts:", result["fraud_alerts"])
        print("\n" + result["financial_report"])