import streamlit as st
import yfinance as yf

# Streamlit App Interface
st.title("Natural Language Financial Data Search")
st.write("Ask about stock prices or financial data!")

# Static list of example queries mapped to stock symbols
example_queries = {
    "What is Apple's stock price?": "AAPL",
    "What is Google's stock price?": "GOOG",
    "What is Amazon's stock price?": "AMZN",
    "What is Microsoft's stock price?": "MSFT",
    "What is Tesla's stock price?": "TSLA"
}

# Function to get stock price using yfinance
def get_stock_price(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1d")
    return data['Close'].iloc[-1]

# User input for natural language query
query = st.text_input("Enter your question (e.g., 'What is Apple's stock price?'):")

# Process query and fetch data using static examples
if st.button("Search"):
    if query:
        # Check if the query matches any of the example queries
        if query in example_queries:
            ticker = example_queries[query]
            try:
                price = get_stock_price(ticker)
                st.success(f"The current stock price of {ticker.upper()} is ${price:.2f}")
            except Exception as e:
                st.error(f"Error fetching data for {ticker.upper()}: {e}")
        else:
            st.warning("Sorry, I don't recognize that query. Please ask about a stock from the examples.")
