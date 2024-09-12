import yfinance as yf
import streamlit as st
import pandas as pd

# Streamlit app title
st.title('NSE Stock Prices and Fundamental Analysis')

# User input for multiple stock symbols and period
symbols = st.text_input("Enter NSE stock symbols separated by commas (e.g., 'RELIANCE.NS,TCS.NS')", "RELIANCE.NS,TCS.NS")
period = st.selectbox("Select the period for stock history:", ['1d', '5d', '1mo', '3mo', '6mo', '1y', '5y', 'max'])

# Button to fetch data
if st.button('Get Stock Data'):
    stock_symbols = [symbol.strip() for symbol in symbols.split(",")]
    
    all_stock_data = {}
    fundamental_data = []
    
    # Fetch data for each stock symbol
    for symbol in stock_symbols:
        stock_data = yf.Ticker(symbol)
        stock_price = stock_data.history(period=period)

        if stock_price.empty:
            st.error(f"No data found for {symbol}.")
        else:
            st.subheader(f"Stock Price Data for {symbol}")
            st.write(stock_price)

        # Fetch fundamental data for each stock
        stock_info = stock_data.info
        
        # Append fundamental data to a list for later display in a table
        fundamental_data.append({
            'Symbol': symbol,
            'Company Name': stock_info.get('longName', 'N/A'),
            'Sector': stock_info.get('sector', 'N/A'),
            'Industry': stock_info.get('industry', 'N/A'),
            'Market Cap': stock_info.get('marketCap', 'N/A'),
            'P/E Ratio': stock_info.get('forwardPE', 'N/A'),
            'P/B Ratio': stock_info.get('priceToBook', 'N/A'),
            'Dividend Yield': stock_info.get('dividendYield', 'N/A'),
            '52 Week High': stock_info.get('fiftyTwoWeekHigh', 'N/A'),
            '52 Week Low': stock_info.get('fiftyTwoWeekLow', 'N/A'),
            'Beta (Volatility)': stock_info.get('beta', 'N/A'),
            'ROE': stock_info.get('returnOnEquity', 'N/A'),
            'EPS': stock_info.get('trailingEps', 'N/A')
        })

    # Convert fundamental data to a DataFrame and display it as a table
    if fundamental_data:
        st.subheader("Fundamental Analysis for Selected Stocks")
        fundamental_df = pd.DataFrame(fundamental_data)
        st.write(fundamental_df)
