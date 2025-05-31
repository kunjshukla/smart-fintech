import csv
import os

def parse_transactions(file_path="data/transactions.csv"):
    """
    Parse transactions from a CSV file.
    Expected CSV format: date,amount,description
    Returns a list of transaction strings.
    """
    transactions = []
    if not os.path.exists(file_path):
        return transactions  # Return empty list if file doesn't exist

    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            amount = row['amount']
            description = row['description']
            transactions.append(f"${amount} to {description}")
    return transactions