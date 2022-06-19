import streamlit as st
import yfinance as yf
import pandas as pd

st.title('Crypto Tracker')

tickers = ('BTC-USD', 'ETH-USD', 'USDT-USD', 'USDC-USD', 'DOGE-USD', 'SOL-USD', 'BNB-USD', 'BUSD-USD', 'ADA-USD', 'XRP-USD')

# About section
expander_bar = st.expander("About")
expander_bar.markdown("""
* **Python libraries:** 
* **Data source:** YahooFinance
""")

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
    # cumulative return
    tot_df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.header('Cumulative Returns of {}'.format(dropdown))
    st.line_chart(tot_df)
    cumret_df = yf.download(dropdown, start, end)['Adj Close']
    st.header('Total Returns of {}'.format(dropdown))
    st.line_chart(cumret_df)
    # df = yf.download(dropdown, start=pd.to_datetime(('today')), end=pd.to_datetime(('today')), interval='1d', group_by='column')
    # st.dataframe(df)
else:
    st.markdown("""
    Input your options in the sidebar on the left to get started!""")

