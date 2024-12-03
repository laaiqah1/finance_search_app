import streamlit as st
import openai
import yfinance as yf

# Set up OpenAI API Key
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit App Interface
st.title("Natural Language Financial Data Search")
st.write("Ask about stock prices or financial data!")

# User input for natural language query
query = st.text_input("Enter your question (e.g., 'What is Apple's stock price?'):")

def process_query(query):
    # Use OpenAI to interpret the query and extract the stock ticker
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",  # Use 'gpt-3.5-turbo-instruct' or GPT-4 if available
        prompt=f"Extract the stock ticker symbol or financial information needed from this query: {query}",
        max_tokens=50
    )
    return response.choices[0].text.strip()

# Function to get stock data
def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data['Close'].iloc[-1]

# Process query and fetch data
if st.button("Search"):
    if query:
        ticker = process_query(query)
        if ticker:
            try:
                price = get_stock_price(ticker)
                st.success(f"The current stock price of {ticker.upper()} is ${price:.2f}")
            except Exception as e:
                st.error(f"Could not retrieve data for {ticker.upper()}. Error: {e}")
        else:
            st.warning("Couldn't determine the stock symbol. Please try again.")

