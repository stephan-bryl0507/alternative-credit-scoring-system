# 💳 Alternative Credit Scoring Model

**Hackathon Project — Fair, Transparent Credit Scoring using Non-Traditional Data Sources**

---

## 🧠 Problem Statement

Traditional credit scoring systems often exclude people with limited or no credit history, leaving millions unbanked or underbanked. In the U.S. alone, approximately **49 million people** are "credit invisible."

Our goal is to build a **credit scoring model** using **alternative data** such as:
- Rent payments
- Utility bills
- Cash flow patterns
- Employment or education history

---

## 🎯 Objectives

- ✅ Ingest and process alternative financial data
- ✅ Build a machine learning model to predict creditworthiness
- ✅ Ensure fairness and interpretability of model predictions
- ✅ Provide user-level explanations for approvals/rejections
- ✅ Visual dashboard for users to understand and improve their score

---

## ✨ Bonus Features

- 📊 **User Dashboard:** Visualize personal score and contributing factors
- 🧑‍🏫 **Financial Coaching:** Get suggestions to improve creditworthiness

---

## 🧱 Tech Stack

| Layer         | Tools/Frameworks                      |
|--------------|----------------------------------------|
| Language      | Python                                |
| Data Analysis | Pandas, NumPy                         |
| Modeling      | Scikit-learn, XGBoost                 |
| Explainability| SHAP, LIME                            |
| Dashboard     | Streamlit / Dash                      |
| Deployment    | (Optional) Streamlit Cloud / Heroku   |

---

## 🗂️ Project Structure

---

## 🛠️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/stephan-bryl0507/alternative-credit-scoring-system/
cd alternative-credit-scoring-system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Dashboard
```bash
streamlit run app.py
```

---

## 📊 Example Use Case

A freelance worker with no traditional credit history has:
- Consistent rent payments for 18 months
- Regular utility bill payments
- Stable income through digital wallet transactions

Our model will analyze this data and give them a fair credit score — potentially opening access to loans.

---

## ⚖️ Fairness & Transparency

We use:
- **SHAP** for model explainability
- **Fairness metrics** to detect bias across demographic groups
- **User-friendly explanations** for each approval/denial

---

## 🧑‍💻 Team Members

- Sanjanaa A (Frontend)
- Stephan Bryl (Backend)
- Deepika S (Testing and debugger)
- Srimathi G (Model and Algorithm Development)
- Tarunkumar.T (Planning and debugging)

---

## 🧾 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## ❤️ Acknowledgments

Built with passion at Error404!  
Inspired by the mission to make credit more **inclusive**, **fair**, and **transparent**.
