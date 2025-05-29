from langchain_openai import ChatOpenAI
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
import pandas as pd

def query_agent(data, query):
    try:
        data.seek(0)
        df = pd.read_csv(data, encoding="utf-8")
    except UnicodeDecodeError:
        data.seek(0)
        df = pd.read_csv(data, encoding="latin1")

    # Limit DataFrame to first 100 rows and 10 columns to avoid token limit errors
    MAX_ROWS = 20
    MAX_COLS = 5
    if len(df) > MAX_ROWS:
        df = df.head(MAX_ROWS)
    if len(df.columns) > MAX_COLS:
        df = df[df.columns[:MAX_COLS]]

    llm = ChatOpenAI(model_name="gpt-4", temperature=0)
    agent = create_pandas_dataframe_agent(llm, df, verbose=False, allow_dangerous_code=True)
    response = agent.invoke({"input": query})
    return response["output"] if isinstance(response, dict) and "output" in response else str(response)