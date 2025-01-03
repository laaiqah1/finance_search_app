import streamlit as st
import yfinance as yf

# Streamlit App Interface
st.title("Natural Language Financial Data Search")
st.write("Ask about stock prices or financial data!")

# Static list of example queries mapped to stock symbols (100 stocks)
example_queries = {
    "What is Apple's stock price?": "AAPL",
    "What is Google's stock price?": "GOOG",
    "What is Amazon's stock price?": "AMZN",
    "What is Microsoft's stock price?": "MSFT",
    "What is Tesla's stock price?": "TSLA",
    "What is Meta's stock price?": "META",
    "What is Nvidia's stock price?": "NVDA",
    "What is Berkshire Hathaway's stock price?": "BRK.B",
    "What is Walmart's stock price?": "WMT",
    "What is Johnson & Johnson's stock price?": "JNJ",
    "What is Procter & Gamble's stock price?": "PG",
    "What is Visa's stock price?": "V",
    "What is Home Depot's stock price?": "HD",
    "What is Coca-Cola's stock price?": "KO",
    "What is PepsiCo's stock price?": "PEP",
    "What is McDonald's stock price?": "MCD",
    "What is Intel's stock price?": "INTC",
    "What is Abbott Laboratories' stock price?": "ABT",
    "What is Merck's stock price?": "MRK",
    "What is Cisco's stock price?": "CSCO",
    "What is Verizon's stock price?": "VZ",
    "What is AT&T's stock price?": "T",
    "What is IBM's stock price?": "IBM",
    "What is Netflix's stock price?": "NFLX",
    "What is Adobe's stock price?": "ADBE",
    "What is Salesforce's stock price?": "CRM",
    "What is General Electric's stock price?": "GE",
    "What is Lockheed Martin's stock price?": "LMT",
    "What is Boeing's stock price?": "BA",
    "What is Goldman Sachs' stock price?": "GS",
    "What is American Express' stock price?": "AXP",
    "What is Morgan Stanley's stock price?": "MS",
    "What is JPMorgan Chase's stock price?": "JPM",
    "What is Citigroup's stock price?": "C",
    "What is Bank of America's stock price?": "BAC",
    "What is Wells Fargo's stock price?": "WFC",
    "What is Square's stock price?": "SQ",
    "What is Shopify's stock price?": "SHOP",
    "What is Snap's stock price?": "SNAP",
    "What is Twitter's stock price?": "TWTR",
    "What is Spotify's stock price?": "SPOT",
    "What is Pinterest's stock price?": "PINS",
    "What is Uber's stock price?": "UBER",
    "What is Lyft's stock price?": "LYFT",
    "What is Roku's stock price?": "ROKU",
    "What is Zoom's stock price?": "ZM",
    "What is DoorDash's stock price?": "DASH",
    "What is Peloton's stock price?": "PTON",
    "What is Airbnb's stock price?": "ABNB",
    "What is Etsy's stock price?": "ETSY",
    "What is Target's stock price?": "TGT",
    "What is Lowe's stock price?": "LOW",
    "What is Best Buy's stock price?": "BBY",
    "What is Macy's stock price?": "M",
    "What is Kohl's stock price?": "KSS",
    "What is Nordstrom's stock price?": "JWN",
    "What is Kroger's stock price?": "KR",
    "What is Walgreens' stock price?": "WBA",
    "What is CVS Health's stock price?": "CVS",
    "What is Home Depot's stock price?": "HD",
    "What is Target's stock price?": "TGT",
    "What is Costco's stock price?": "COST",
    "What is Chipotle's stock price?": "CMG",
    "What is McDonald's stock price?": "MCD",
    "What is Wendy's stock price?": "WEN",
    "What is Domino's Pizza's stock price?": "DPZ",
    "What is Papa John's stock price?": "PZZA",
    "What is Starbucks' stock price?": "SBUX",
    "What is Dunkin' Brands' stock price?": "DNKN",
    "What is Yum! Brands' stock price?": "YUM",
    "What is Shake Shack's stock price?": "SHAK",
    "What is Wingstop's stock price?": "WING",
    "What is Bloomin' Brands' stock price?": "BLMN",
    "What is Darden Restaurants' stock price?": "DRI",
    "What is Hilton's stock price?": "HLT",
    "What is Marriott's stock price?": "MAR",
    "What is American Airlines' stock price?": "AAL",
    "What is Delta's stock price?": "DAL",
    "What is Southwest Airlines' stock price?": "LUV",
    "What is United Airlines' stock price?": "UAL",
    "What is Alaska Air's stock price?": "ALK",
    "What is JetBlue's stock price?": "JBLU",
    "What is Carnival's stock price?": "CCL",
    "What is Royal Caribbean's stock price?": "RCL",
    "What is Norwegian Cruise Line's stock price?": "NCLH",
    "What is Expedia's stock price?": "EXPE",
    "What is Booking Holdings' stock price?": "BKNG",
    "What is Priceline's stock price?": "PCLN",
    "What is TripAdvisor's stock price?": "TRIP",
    "What is Airbnb's stock price?": "ABNB",
    "What is Lyft's stock price?": "LYFT",
    "What is Uber's stock price?": "UBER",
    "What is Snap's stock price?": "SNAP",
    "What is Pinterest's stock price?": "PINS",
    "What is Twitter's stock price?": "TWTR",
    "What is Spotify's stock price?": "SPOT",
    "What is Zoom's stock price?": "ZM",
    "What is Adobe's stock price?": "ADBE",
    "What is Salesforce's stock price?": "CRM",
    "What is DocuSign's stock price?": "DOCU",
    "What is Autodesk's stock price?": "ADSK",
    "What is Intuit's stock price?": "INTU",
    "What is Microsoft Corp.'s stock price?": "MSFT",
    "What is Oracle's stock price?": "ORCL",
    "What is SAP's stock price?": "SAP",
    "What is Palantir's stock price?": "PLTR",
    "What is Snowflake's stock price?": "SNOW",
    "What is Square's stock price?": "SQ"
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
