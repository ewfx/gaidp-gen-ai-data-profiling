# 🚀 Project Name
Team - Data-Profiling

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
Generate a Gen AI – based data profiling that can:

1. Extract, interpret, and refine regulatory reporting instructions to identify key data validation requirements.
2.  Automatically generate profiling rules based on allowable values and cross relation between the elements using LLM or ML.
3. Generate executable validation code to assess whether the reported data conforms to the extracted rules.
4. Suggested remediation actions for flagged transactions/observations, including automated explanations for auditors.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [Video Demo](#) (if applicable)  

🖼️ Screenshots:
Here is the Architecture diagram.
![image](https://github.com/user-attachments/assets/4e8aead4-0735-419a-8b90-f9ee0d58b880)


## ⚙️ What It Does
Gen AI based Data Profiling.

## 🚧 Challenges We Faced
There was an issue accessing OpenAi API due to the API hits limit being exdeeded.

## 🏃 How to Run
1. Run the python script **GenAI_DataProfiling.py**.
   example: python GenAI_DataProfiling.py
   Place the rulesset.json in the current directory which has which has the predifined rulesets.

2. In the above script the function validate_transaction(test_transaction) is present which can be used to perform ruleset validation.
   example: python testcript.py   (test script present in the test directory)
   
   ```

## 🏗️ Tech Stack
- 🔹 OpenAI: For generating ruleset and python validation code
- 🔹 Python: For implementing the DQ pipeline
- 🔹 Json/Csv: For storing rule sets/invalid transactions
- 🔹 Draw.io: For architecture diagram creation


## 👥 Team
Girichandu Palakodeti
Jagadeesh Ganaparthi
Balaji Buddana
Venkatesh Bandi
Praveen Lingampate

