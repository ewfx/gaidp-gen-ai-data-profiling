# Sample transaction with intentional errors
test_transaction = {
    "CustomerID": "123456",
    "InternalObligorID": "654321",
    "OriginalInternalObligorID": "111111",
    "ObligorName": "Test Corp",
    "City": "New York",
    "Country": "US",  # Invalid, should be 2 characters
    "Zip Code": "12345",  # Invalid, should be a valid ZIP or postal code
    "IndustryCode": "9999",  # Valid
    "IndustryCodeType": "SIC",  # Invalid, should be "NAICS", "SIC", or "GICS"
    "StockExchange": "BSE",  # Invalid, should be NYSE, NASDAQ, LSE, TSX
    "TKR": "AAPL",
    "CUSIP": "123456",  # Invalid, should be 6 digits or "NA"
    "MaturityDate": "2024/05/15"  # Invalid, should be in "yyyy-mm-dd" format
}

# Run validation
result = validate_transaction(test_transaction)

# Print result
print(result)
