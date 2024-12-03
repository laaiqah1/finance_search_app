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

# Function to process the query using OpenAI API
def process_query(query):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use the appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": f"Extract the stock ticker symbol from: {query}"}
            ],
            max_tokens=50
        )
        result = response['choices'][0]['message']['content'].strip()
        return result
    except Exception as e:
        st.error(f"Error with OpenAI API: {e}")
        return None

# Function to get stock data
def get_stock_price(ticker):
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="1d")
        return data['Close'].iloc[-1]
    except Exception as e:
        st.error(f"Could not retrieve data for {ticker.upper()}. Error: {e}")
        return None

# Process query and fetch data
if st.button("Search"):
    if query:
        ticker = process_query(query)
        if ticker:
            st.write(f"Extracted Ticker: {ticker}")  # Debug: Show extracted ticker
            # Ensure ticker is valid (only letters)
            if ticker.isalpha():
                price = get_stock_price(ticker)
                if price is not None:
                    st.success(f"The current stock price of {ticker.upper()} is ${price:.2f}")
                else:
                    st.warning(f"Could not retrieve stock price for {ticker.upper()}.")
            else:
                st.warning(f"Invalid ticker symbol: {ticker}. Please provide a valid symbol.")
        else:
            st.warning("Couldn't determine the stock symbol. Please try again.")
    else:
        st.warning("Please enter a query.")
