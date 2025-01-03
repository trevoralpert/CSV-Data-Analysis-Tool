
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI

def query_agent(data, query):
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(data)

    # Initialize the OpenAI model
    llm = ChatOpenAI(model_name="gpt-4", temperature=0)

    # Create a custom prompt template for CSV analysis
    prompt = PromptTemplate(
        input_variables=["query", "dataframe"],
        template=(
            "You are an AI specialized in analyzing tabular data. Here is the data:\n\n{dataframe}\n\n"
            "Respond to the following query: {query}"
        ),
    )

    # Format the data and query
    formatted_prompt = prompt.format(query=query, dataframe=df.to_string())

    # Get the response
    response = llm.predict(formatted_prompt)
    return response