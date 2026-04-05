# 💰 AI Financial Advisor

An intelligent **AI-powered personal finance management system** built using **Python & Streamlit**.  
This application helps users track expenses, plan budgets, monitor EMIs, and get AI-driven financial advice.

---

## 🚀 Features

### 🔐 Authentication
- Secure user login system
- User-specific financial data storage

### 💸 Expense Tracker
- Add, update, and delete expenses
- Categorize spending (Food, Travel, Bills, etc.)
- View expense history

### 📊 Budget Planner
- Set monthly budgets
- Track budget vs actual spending
- Alerts when exceeding budget

### 🏦 EMI Tracker
- Manage loan/EMI details
- Track monthly payments
- Remaining balance calculation

### 📈 Reports Dashboard
- Visual insights of spending
- Category-wise analysis
- Monthly trends

### 🤖 AI Financial Advisor
- Smart financial suggestions
- Budget optimization tips
- Savings recommendations

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** SQLite (`finance.db`)
- **AI Integration:** Custom AI logic / LLM APIs (Groq/OpenAI compatible)
- **Styling:** CSS

---

## 📋 Setup Instructions

### Prerequisites
- Python 3.8+
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ayanstringer2002/Capstone_Final_Year_Project.git
   cd Capstone_Final_Year_Project
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **For AI Features (Optional)**
   - Get a free Groq API key from [https://console.groq.com/keys](https://console.groq.com/keys)
   - Create a `.env` file in the project root:
     ```
     GROQ_API_KEY=your_api_key_here
     ```
   - Or set environment variable: `export GROQ_API_KEY=your_key`

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

### Deployment

- **Streamlit Cloud**: Connect your GitHub repo and deploy
- **Local**: Use the run command above
- **AI Features**: Add `GROQ_API_KEY` to Streamlit Cloud secrets for deployment

### CI/CD Pipeline

This project includes GitHub Actions for automated testing:

- **Automated Tests**: Runs on every push/PR to main branch
- **Code Quality**: Checks formatting, linting, and import sorting
- **Dependency Checks**: Validates all required packages
- **Import Tests**: Ensures all modules load correctly

---

## 📁 Project Structure

## 📁 Project Structure

```
├── app.py                 # Main application
├── requirements.txt       # Python dependencies
├── assets/
│   └── style.css         # Custom styling
├── database/
│   └── db.py            # Database operations
├── pages/                # Streamlit pages
│   ├── 1_Login.py
│   ├── 2_Expense_Tracker.py
│   ├── 3_Budget_Planner.py
│   ├── 4_EMI_Tracker.py
│   ├── 5_Reports_Dashboard.py
│   └── 6_AI_Financial_Advisor.py
└── utils/                # Utility modules
    ├── ai_budget.py
    ├── alerts.py
    ├── auth.py
    ├── groq_ai.py
    └── helpers.py
```

---


## ⚙️ Installation & Setup

###  Clone the repository

```bash
git clone https://github.com/your-username/ai-financial-advisor.git
cd ai-financial-advisor
```

###  Create Virtual Environemnt and Activate it on windows/Macos/Linux
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

## Install The Requirements 
```bash
pip install -r requirements.txt

```
## Setup environment variables

Create a `.env` file in the root directory and add your API keys:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🤝 Contributing

We welcome contributions! This project uses GitHub Actions for CI/CD.

- **CI/CD Status**: Check the Actions tab for pipeline status
- **Tests**: All changes must pass automated tests
- **Code Style**: Follow PEP 8 and use Black for formatting

---
```bash
API_KEY=your_api_key_here
```

## Run the App
```bash
streamlit run app.py
```

## Future Improvements
- 🔗 Bank API integration
- 📱 Mobile responsive UI
- ☁️ Cloud deployment

## Members 
- Tanweer Iqbal
- Aditya Vikram singh
- Kamal Yadav
- Ayan Ahmad
- Saurabh Yadav

## Contributors
- Tanveer Iqbal  
  Contributed to the development of the Expense Tracker module, including adding and managing daily expenses with details like date, category, type, and amount.  
  Also assisted in project documentation, report writing, system integration, and preparation of the final project presentation.




