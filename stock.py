#!/usr/bin/env python
# coding: utf-8

# # Stock price app for US companies

# In[6]:



#import necessary passages
import yfinance as yf #we used Yahoo finance
import pandas as pd
import streamlit as st


#title
st.title(':blue[Stock Price Chart for US companies]')

#code
stock='GOOGL'#Enter the name of the stock
stockdata=yf.Ticker(stock)
stockdf=stockdata.history(period='1d', start='2013-07-03', end='2023-07-03') #we have taken a 10 year period and 1 day closing 

#output
st.subheader(':red[Closing price Chart]')
st.line_chart(stockdf.Close) #x-axis represents day and y-axis represents Closing price

st.subheader(':green[Volume Chart]') 
st.line_chart(stockdf.Volume)  #x-axis represents day and y-axis represents Volume


# In[ ]:




