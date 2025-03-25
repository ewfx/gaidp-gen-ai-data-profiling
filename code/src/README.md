# Rule Set Generation and Python Validation DQ Workflow

## 🚀 **Overview**
This project implements a **Data Quality (DQ) Validation Workflow** with **Rule Set Generation using Generative AI**. The solution ensures that data quality rules are generated dynamically using AI models and then validated through a Python-based DQ pipeline. Invalid records are captured, and valid records proceed to the final output.

---

## ⚙️ **Technologies Used**
- **OpenAI**: For generating rule sets using Gen AI and prompt engineering.
- **Python**: For validation workflows and data processing.
- **JSON**: To store and append the generated rule sets.
- **CSV**: For storing invalid observation transactions.
- **Draw.io**: For architecture diagram creation.

---

## 🛠️ **Installation Instructions**
1. **Clone the Repository**
```bash
git clone <repository_url>
cd <repository_folder>

2. **Install Dependencies**

bash
Copy
Edit
pip install -r requirements.txt

3. **Set Up Environment Variables**

Create a .env file with the following variables:

ini
OPENAI_API_KEY=<YOUR_OPENAI_API_KEY>



🚦 **Workflow Description**

🔥 **1. Rule Set Generation using Gen AI**

Prompt Engineering:

Few-shot learning and other techniques are used to create prompts.

OpenAI Model:

The prompts are sent to the OpenAI model, which generates data validation rules.

Rule Set Operations:

The rules are either:

Updated in the existing ruleset.json file.

Appended to the ruleset.json file as new rules.

Final Validation and Enhancement:

The generated rules are validated and enhanced by refining the prompt engineering process.

🔥 **2. Python Validation DQ Workflow**
Reading Rule Set:

The Python workflow reads the ruleset.json file containing the validation rules.

Data Generation for Testing:

Synthetic or real data is generated for testing against the rules.

DQ Validation:

The data quality validation process performs checks:

Invalid records → Stored in observation_transactions.csv.

Valid records → Proceed to the final output.

🛠️ **Architecture Diagram**
The architecture of the solution is shown below:




✅ Ensure you add the image file architecture.jpg to your repository and reference it in the README.md.

📊 **Usage Guide**
1.** Generate Rules Using Gen AI**

python generate_rules.py --prompt "Generate DQ rules for customer data"

2. **Run DQ Validation**
python dq_validation.py --input test_data.csv --rules ruleset.json --output output.csv

👥 Contributors
[Your Name] – Data Engineer

Feel free to submit pull requests or report issues.

