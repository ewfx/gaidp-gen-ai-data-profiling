import random
import pandas as pd
import json

# Load ruleset from file
def load_ruleset(file_path="ruleset.json"):
    with open(file_path, "r") as file:
        return json.load(file)

ruleset = load_ruleset()

# Generate sample transactions
def generate_transactions(n=1000000, invalid_ratio=0.1):
    transactions = []
    for _ in range(n):
        transaction = {
            "CustomerID": str(random.randint(100000, 999999)),
            "InternalObligorID": str(random.randint(100000, 999999)),
            "OriginalInternalObligorID": str(random.randint(100000, 999999)),
            "ObligorName": random.choice(["ABC Corp", "XYZ Ltd", "John Doe", "Jane Smith"]),
            "City": random.choice(["New York", "Los Angeles", "Chicago", "San Francisco"]),
            "Country": random.choice(["US", "GB", "CA", "AU"]),  # Valid ISO 3166-1 alpha-2 codes
            "Zip Code": random.choice(["12345", "98765", "A1B 2C3", "SW1A 1AA"]),  # US & Foreign postal codes
            "IndustryCode": random.choice(["5411", "7225", "1001", "GICS12", "SIC9999"]),  # Some valid & invalid cases
            "StockExchange": random.choice(["NYSE", "NASDAQ", "LSE", "TSX", "INVALID_EX"]),
            "TKR": random.choice(["AAPL", "GOOGL", "AMZN", "NA"]),
            "CUSIP": random.choice(["123456", "654321", "111111", "NA", "INVALID"])
        }

        # Inject some invalid data
        if random.random() < invalid_ratio:
            field = random.choice(list(transaction.keys()))
            if field in ["CustomerID", "InternalObligorID", "OriginalInternalObligorID", "ObligorName"]:
                transaction[field] += random.choice(["\n", ",", "\r", "\x00"])
            elif field == "Country":
                transaction[field] = random.choice(["USA", "123", "us", ""])
            elif field == "Zip Code":
                transaction[field] = random.choice(["1234", "0000A", "ABCDE", ""])
            elif field == "IndustryCode":
                transaction[field] = random.choice(["abc123", "123", "1234567", ""])
            elif field == "StockExchange":
                transaction[field] = random.choice(["INVALID", "1234", "NotAnExchange", ""])
            elif field == "TKR":
                transaction[field] = random.choice(["INVALID", "", "123456"])
            elif field == "CUSIP":
                transaction[field] = random.choice(["ABCDEF", "12345", "NA", "INVALIDCUSIP"])

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
            if field == "ObligorName" and value in ["John Doe", "Jane Smith"]:
                observations.append(f"{field} should be replaced with 'Individual'.")
            if field == "Country":
                if len(value) != 2:
                    observations.append(f"{field} must be exactly 2 characters.")
                if not value.isupper():
                    observations.append(f"{field} must be in uppercase.")
                if value not in ["US", "GB", "CA", "AU"]:
                    observations.append(f"{field} must be a valid ISO 3166-1 alpha-2 country code.")
                if value == "":
                    observations.append(f"{field} cannot be null or empty.")
            if field == "StockExchange" and value not in ["NYSE", "NASDAQ", "LSE", "TSX"]:
                observations.append(f"{field} must be a valid stock exchange (NYSE, NASDAQ, LSE, TSX).")
            if field == "TKR" and value not in ["AAPL", "GOOGL", "AMZN", "NA"]:
                observations.append(f"{field} must be a valid stock ticker or 'NA'.")
            if field == "CUSIP" and (len(value) != 6 or not value.isalnum()):
                observations.append(f"{field} must be a valid 6-character alphanumeric CUSIP or 'NA'.")

    return "; ".join(observations) if observations else "Valid"

# Generate transactions and validate
data = generate_transactions()
df = pd.DataFrame(data)
df["Observations"] = df.apply(validate_transaction, axis=1)

# Filter only invalid transactions
df_invalid = df[df["Observations"] != "Valid"]

# Save to CSV
df_invalid.to_csv("observation_transactions.csv", index=False)
print("Validation complete. Data saved to validated_transactions.csv")
