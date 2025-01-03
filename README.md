# CSV Query Analysis App

A simple Streamlit-based application that leverages OpenAI's GPT-4 model to analyze CSV files and respond to user queries. The app uses LangChain to build custom prompts for CSV analysis and provides quick insights based on user-provided data and queries.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Example Queries](#example-queries)
- [Contributing](#contributing)
- [License](#license)

## Overview

The app enables users to upload a CSV file, input a natural language query, and receive insights or analyses based on the data in the file. It is particularly useful for non-technical users who want to explore tabular data interactively.

## Features
- Upload CSV files directly through the interface.
- Ask natural language queries about your data.
- Leverages OpenAI's GPT-4 for intelligent data analysis.
- Simple and intuitive Streamlit interface.

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For creating an interactive web app.
- **LangChain**: For building AI chains and managing the query pipeline.
- **OpenAI GPT-4**: For language processing and intelligent responses.
- **Pandas**: For data manipulation and analysis.
- **dotenv**: For environment variable management.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/trevoralpert/csv-query-analysis-app.git
   cd csv-query-analysis-app
