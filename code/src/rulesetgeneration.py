import os
import json
import openai

# Load API Key from environment variables (Recommended)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Load existing ruleset from ruleset.json
def load_ruleset():
    try:
        with open("ruleset.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Save updated ruleset back to ruleset.json
def save_ruleset(ruleset):
    with open("ruleset.json", "w") as file:
        json.dump(ruleset, file, indent=4)

# Function to call the API to generate rules
def generate_rule(field_data):
    prompt = f"""
    Input:
    {json.dumps(field_data, indent=4)}

    Output:
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "You are an expert in generating validation rules for structured data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )
    
    output_text = response["choices"][0]["message"]["content"]
    
    # Convert the generated output to a dictionary format
    try:
        rule_json = json.loads(output_text)
        return rule_json
    except json.JSONDecodeError:
        print("Error parsing API response.")
        return None

# Function to update the ruleset
def update_ruleset(field_data):
    ruleset = load_ruleset()
    
    # Generate rule using API
    new_rule = generate_rule(field_data)
    if not new_rule:
        print("Failed to generate rule.")
        return
    
    # Extract the key and constraints from the new rule
    key, value = list(new_rule.items())[0]
    
    # Update existing rule or append a new one
    if key in ruleset:
        ruleset[key]["constraints"] = list(set(ruleset[key]["constraints"] + value["constraints"]))
    else:
        ruleset[key] = value

    # Save the updated ruleset
    save_ruleset(ruleset)
    print(f"Ruleset updated successfully for {key}.")

# Example input
field_data = {
    "FieldNo": 14,
    "FieldName": "CUSIP",
    "TechnicalFieldName": "CUSIP",
    "MDRM": "CLCO9161",
    "Description": "Report the CUSIP of the obligor, if available...",
    "AllowableValues": "Must be valid 6 digit CUSIP number issued by the CUSIP Service Bureau."
}

# Run the update function
update_ruleset(field_data)
