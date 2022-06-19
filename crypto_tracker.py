import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Crypto Tracker')

tickers = ('BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'DOGE-USD', 'SOL-USD', 'BNB-USD', 'BUSD-USD', 'ADA-USD', 'XRP-USD')

# About section
expander_bar = st.expander("About")
expander_bar.markdown("""Use this tracker to compare different cryptocurrencies (tickers) based on their price and cumulative 
returns! From the sidebar on the left, 
you can choose which cryptocurrencies to compare and a timeframe to analyze. 
* **Python libraries:** pandas, streamlit
* **Data source:** YahooFinance""" )

# Columns layout
col1 = st.sidebar
col2, col3 = st.columns((3, 1))

# Sidebar
col1.header('Input Options')
dropdown = col1.multiselect('Pick your assets', tickers)
start = col1.date_input('Start', value=pd.to_datetime('2021-01-01'))
end = col1.date_input('End', value=pd.to_datetime(('today')))

# cumulative return - the total change in the investment price over a set time
def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


if len(dropdown) > 0:
    # summary
    st.header('Today\'s Prices')
    summary_expander = st.expander("Information")
    summary_expander.markdown("""Below is all the data for each ticker for today to help you compare different 
    cryptocurrencies.  
    - **Open** is the price when the market open each day \\
    - **Close** is the price when the market closes for the day \\
    - **High** is the highest price the cryptocurrency reaches each day\\
    - **Low** is the lowest price the cryptocurrency falls to that day\\
    - **Adjusted Close** is the price which reflects that cryptocurrency's value after accounting for any corporate actions""")
    df_list = list()
    for ticker in dropdown:
        data = yf.download(ticker, group_by="Ticker", period='1d')
        data['Ticker'] = ticker  # add this column because the dataframe doesn't contain a column with the ticker
        df_list.append(data)

    # combine all dataframes into a single dataframe
    df = pd.concat(df_list)
    df = df[['Ticker', 'Open', 'Close', 'High', 'Low', 'Adj Close', 'Volume']]
    st.dataframe(df)

    # prices
    st.header('Prices of {} from {} to {}'.format(dropdown, start, end))
    summary_expander = st.expander("What does this chart show?")
    summary_expander.markdown("""The chart below shows the prices for the cryptocurrencies you selected over the 
    given time frame. Cryptocurrencies are a tradable asset, much like stocks, commodities, securities and so on. 
    Their price is determined by how much interest there is on the market in buying them – that's called demand – and 
    how much is available to buy – that's supply. The relationship between the two determines the price. """)
    price_df = yf.download(dropdown, start, end)['Adj Close']
    st.line_chart(price_df)

    # cumulative return
    st.header('Cumulative Returns of {} from {} to {}'.format(dropdown, start, end))
    summary_expander = st.expander("What does cumulative return mean?")
    summary_expander.markdown("""The chart below shows the cumulative return for the cryptocurrencies you selected over the 
        given time frame. A cumulative return on an investment is the aggregate amount that the investment has gained 
        or lost over time, independent of the amount of time involved.  """)
    cumret_df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.line_chart(cumret_df)



else:
    st.markdown("""
    Input your options in the sidebar on the left to get started!""")

