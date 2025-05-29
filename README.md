# CSV Data Analysis Tool

A modern, interactive Streamlit application that leverages OpenAI's GPT-4 and LangChain's Pandas DataFrame Agent to analyze CSV files and answer your data questions in natural language.

---

## 🚀 Features

- **Conversational Chatbot:** Ask questions about your CSV data in plain English.
- **Full DataFrame Analysis:** Uses a code-executing agent to answer questions about the entire dataset (within token limits).
- **Streamlit UI:** Simple, user-friendly web interface for uploading files and chatting.
- **OpenAI GPT-4 Integration:** Harnesses the power of GPT-4 for intelligent data analysis and explanations.
- **Secure by Default:** Dangerous code execution is opt-in and only enabled in local, trusted environments.

---

## 🛠️ Technologies Used

- **Python 3.12+**
- **Streamlit** – Interactive web app framework
- **LangChain** – LLM orchestration and agent tools
- **LangChain-Experimental** – Pandas DataFrame Agent
- **OpenAI GPT-4** – Language model for code and explanations
- **Pandas** – Data manipulation and analysis
- **dotenv** – Environment variable management

---

## ⚡ Quickstart

1. **Clone the repository:**
   ```bash
   git clone https://github.com/trevoralpert/csv-query-analysis-app.git
   cd csv-query-analysis-app
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set your OpenAI API key:**
   - Create a `.env` file in the project root:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

5. **Run the app:**
   ```bash
   streamlit run st_app.py
   ```

---

## 💡 Usage

1. Upload your CSV file using the file uploader.
2. Ask questions about your data in the chat interface (e.g., "Who gave the lowest rating?", "What is the average score?").
3. The app will analyze your data and respond conversationally.

**Note:** For large CSVs, only a sample of the data may be analyzed due to OpenAI token limits.

---

## 🛡️ Security Notice

This app uses LangChain's Pandas DataFrame Agent with `allow_dangerous_code=True`, which allows the LLM to execute Python code on your data.  
**Only use this app in a trusted, local environment. Do not deploy to production or expose to untrusted users.**

For more information, see the [LangChain security documentation](https://python.langchain.com/docs/security/).

---

## 📝 Example Queries

- "What is the highest value in the 'Sales' column?"
- "List all unique customer names."
- "What is the average rating?"
- "Who gave the lowest rating?"

---

## 🤝 Contributing

Pull requests and suggestions are welcome! Please open an issue or submit a PR.

---

## 📄 License

This project is licensed under the MIT License.

---
