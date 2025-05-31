import pandas as pd
def run_financial_analysis(file_path=None, transactions=None, risk_profile="moderate"):
    print(f"\n[DEBUG] Starting financial analysis with risk_profile: {risk_profile}")
    try:
        # Initialize default values
        budget_summary = "Default budget summary"
        investment_advice = "Default investment advice"
        fraud_alerts = "No fraud alerts"
        report = "Financial report will be generated here"

        # Process transactions if provided
        if transactions:
            print("[DEBUG] Processing provided transactions...")
            try:
                transactions_df = pd.DataFrame(transactions)
                print(f"[DEBUG] Processed {len(transactions_df)} transactions")
                budget_summary = f"Processed {len(transactions_df)} transactions"
                
                # Simple fraud detection based on amount
                large_transactions = transactions_df[transactions_df['amount'].abs() > 900]
                if not large_transactions.empty:
                    flagged = large_transactions[['amount', 'description']].to_dict('records')
                    fraud_alerts = "Potential issues found:\n" + "\n".join(
                        f"- ${tx['amount']}: {tx['description']}" 
                        for tx in flagged
                    )
                
            except Exception as e:
                print(f"[WARNING] Error processing transactions: {e}")

        # Generate a simple report
        report = f"""
        Financial Analysis Report
        ========================
        Budget Summary: {budget_summary}
        Risk Profile: {risk_profile}
        Fraud Alerts: {fraud_alerts}
        """

        return {
            "budget_summary": budget_summary,
            "investment_advice": investment_advice,
            "fraud_alerts": fraud_alerts,
            "financial_report": report
        }

    except Exception as e:
        import traceback
        error_msg = f"Error during analysis: {str(e)}\n{traceback.format_exc()}"
        print(f"[ERROR] {error_msg}")
        return {"error": error_msg}