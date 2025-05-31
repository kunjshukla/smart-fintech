import logging
import warnings
import pandas as pd
warnings.filterwarnings("ignore", category=DeprecationWarning, module="paramiko")

# Suppress gRPC logs
logging.getLogger('grpc').setLevel(logging.WARNING)

from core.advisor import run_financial_analysis

if __name__ == "__main__":
    result = run_financial_analysis(
        income=5000,
        expenses=3000,
        risk_profile="moderate"
    )
    
if "error" in result:
    print("Error:", result["error"])
else:
    print("\nFinancial Analysis Results:")
    print("=" * 40)
    print(result["financial_report"])
    
    # Print individual components if needed
    print("\nDetailed Analysis:")
    print("-" * 40)
    print("Budget Summary:", result["budget_summary"])
    print("\nInvestment Advice:", result["investment_advice"])
    print("\nFraud Alerts:", result["fraud_alerts"])