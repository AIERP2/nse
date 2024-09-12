import yfinance as yf
import streamlit as st

# Streamlit app title
st.title('NSE Stock Price and Fundamental Analysis')

# User input for stock symbol and period
symbol = st.text_input("Enter the NSE stock symbol (e.g., 'RELIANCE.NS')", "RELIANCE.NS")
period = st.selectbox("Select the period for stock history:", ['1d', '5d', '1mo', '3mo', '6mo', '1y', '5y', 'max'])

# Button to fetch data
if st.button('Get Stock Data'):
    # Fetch stock data
    stock_data = yf.Ticker(symbol)
    stock_price = stock_data.history(period=period)

    if stock_price.empty:
        st.error(f"No data found for {symbol}.")
    else:
        st.subheader(f"Stock Price Data for {symbol}")
        st.write(stock_price)

    # Fetch fundamental data
    stock_info = stock_data.info
    st.subheader(f"Fundamental Analysis for {symbol}")

    # Display key financial metrics in columns
    col1, col2 = st.columns(2)

    col1.write(f"**Company Name:** {stock_info.get('longName', 'N/A')}")
    col1.write(f"**Sector:** {stock_info.get('sector', 'N/A')}")
    col1.write(f"**Industry:** {stock_info.get('industry', 'N/A')}")
    col1.write(f"**Market Cap:** {stock_info.get('marketCap', 'N/A')}")
    col1.write(f"**P/E Ratio:** {stock_info.get('forwardPE', 'N/A')}")
    col1.write(f"**P/B Ratio:** {stock_info.get('priceToBook', 'N/A')}")

    col2.write(f"**Dividend Yield:** {stock_info.get('dividendYield', 'N/A')}")
    col2.write(f"**52 Week High:** {stock_info.get('fiftyTwoWeekHigh', 'N/A')}")
    col2.write(f"**52 Week Low:** {stock_info.get('fiftyTwoWeekLow', 'N/A')}")
    col2.write(f"**Beta (Volatility):** {stock_info.get('beta', 'N/A')}")
    col2.write(f"**Return on Equity (ROE):** {stock_info.get('returnOnEquity', 'N/A')}")
    col2.write(f"**EPS (Earnings Per Share):** {stock_info.get('trailingEps', 'N/A')}")
