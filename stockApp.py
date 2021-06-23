#!/usr/bin/env python
# coding: utf-8

# In[4]:


import yfinance as yf
import streamlit as st
import pandas as pd


# In[5]:


st.write("""

""")


# In[6]:


tickerSymbol = 'GOOGL'
tickerData =  yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period = 'id', start = '2010-05-01', end = '2021-06-01')
tickerDf


# In[7]:


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)


# In[ ]:




