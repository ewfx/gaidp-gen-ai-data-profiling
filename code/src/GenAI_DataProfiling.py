import random
import pandas as pd
import json
import re
from datetime import datetime

# Load ruleset from file
def load_ruleset(file_path="ruleset.json"):
    with open(file_path, "r") as file:
        return json.load(file)

ruleset = load_ruleset()



# Generate sample transactions
def generate_transactions(n, invalid_ratio=0.1):
    transactions = []
    for _ in range(n):
        transaction = {
            "CustomerID": str(random.randint(100000, 999999)),
            "InternalObligorID": str(random.randint(100000, 999999)),
            "OriginalInternalObligorID": str(random.randint(100000, 999999)),
            "ObligorName": random.choice(["ABC Corp", "XYZ Ltd", "John Doe", "Jane Smith"]),
            "City": random.choice(["New York", "Los Angeles", "Chicago", "San Francisco"]),
            "Country": random.choice(["US", "GB", "CA", "AU"]),
            "Zip Code": random.choice(["12345", "98765", "A1B 2C3", "SW1A 1AA"]),
            "IndustryCode": random.choice(["5411", "7225", "1001", "GICS12", "SIC9999"]),
            "IndustryCodeType": random.choice(["NAICS", "SIC", "GICS"]),
            "StockExchange": random.choice(["NYSE", "NASDAQ", "LSE", "TSX", "INVALID_EX"]),
            "TKR": random.choice(["AAPL", "GOOGL", "AMZN", "NA"]),
            "CUSIP": random.choice(["123456", "654321", "111111", "NA", "INVALID"]),
            "MaturityDate": random.choice(["2024-05-15", "2023-12-31", "2024/05/15", "15-05-2024"])  # Some invalid cases
        }
        transactions.append(transaction)

    return transactions

# Function to validate transactions
def validate_transaction(transaction):
    observations = []

    for field, value in transaction.items():
        if field in ruleset:
            constraints = ruleset[field]["constraints"]

            if "no_carriage_return" in constraints and "\r" in value:
                observations.append(f"{field} contains a carriage return.")
            if "no_line_feed" in constraints and "\n" in value:
                observations.append(f"{field} contains a line feed.")
            if "no_comma" in constraints and "," in value:
                observations.append(f"{field} contains a comma.")
            if "no_unprintable" in constraints and any(ord(char) < 32 for char in value):
                observations.append(f"{field} contains unprintable characters.")

            if field == "IndustryCode":
                if not re.fullmatch(r"\d{4}|[A-Z]+\d+", value):
                    observations.append(f"{field} must be a valid numeric SIC or GICS code.")
            
            if field == "IndustryCodeType":
                if value not in ["NAICS", "SIC", "GICS"]:
                    observations.append(f"{field} must be one of: NAICS, SIC, or GICS.")

            if field == "MaturityDate":
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
                    observations.append(f"{field} must be in 'yyyy-mm-dd' format.")
                else:
                    try:
                        datetime.strptime(value, "%Y-%m-%d")
                    except ValueError:
                        observations.append(f"{field} must be a valid calendar date.")

            if field == "CUSIP":
                if not (re.fullmatch(r"[0-9]{6}", value) or value == "NA"):
                    observations.append(f"{field} must be a valid 6-digit CUSIP or 'NA'.")
                if len(value) != 6 and value != "NA":
                    observations.append(f"{field} must be exactly 6 digits or 'NA'.")

            if field == "StockExchange":
                allowed_exchanges = {"NYSE", "NASDAQ", "LSE", "TSX"}  # Define valid exchanges
                if value not in allowed_exchanges:
                    observations.append(f"{field} must be one of {allowed_exchanges}.")

            if field == "Zip Code":
                if not re.fullmatch(r"\d{5}(-\d{4})?|[A-Z]\d[A-Z] \d[A-Z]\d", value):
                    observations.append(f"{field} must be a valid US ZIP code or Canadian postal code.")

            if field == "Country":
                if not re.fullmatch(r"[A-Z]{2}", value):
                    observations.append(f"{field} must be exactly two uppercase letters.")

    return "; ".join(observations) if observations else "Valid"

# Generate transactions and validate
transactions = generate_transactions(1000000)
df = pd.DataFrame(transactions)
df["Observations"] = df.apply(validate_transaction, axis=1)

df_invalid = df[df["Observations"] != "Valid"]
df_invalid.to_csv("invalid_transactions.csv", index=False)
