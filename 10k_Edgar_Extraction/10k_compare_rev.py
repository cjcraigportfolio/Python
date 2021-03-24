#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # for visualization
import yfinance as yf
import seaborn as sns
import re
import requests
import bs4 as bs
from openpyxl import load_workbook


df = pd.read_csv('rev_dict_final_example.csv')
#df.loc[(df['ticker_name'] == company_id1) & (df['industry_group'] == industry_id)]
co = pd.read_csv('tempURL.csv')
co.head()

def ticker_url(tick_col, url_col):
        co_dict = {}
        for k,v in zip(tick_col,url_col):
                co_dict[k] = v
        return co_dict

co_info = ticker_url(co['ticker'],co['url_10k'])



st.title('10k Revenue Comparison')
st.markdown("This application compares the revenue between two different companies")
st.write('')

st.sidebar.title('10k Revenue Comparison')
st.sidebar.write('')

st.sidebar.title("Industry")
industry = df['industry_group'].unique()
# for industry selection
industry_dropdown = st.sidebar.selectbox(
        'Select industry',industry
)
industry_id = industry_dropdown

if pd.isnull(industry_dropdown):
        tickers = df["ticker_name"].unique()
else:
        tickers = df["ticker_name"].loc[df["industry_group"] == industry_dropdown].unique()

# for company selection
st.sidebar.title("Company")
st.sidebar.markdown("Choose companies to compare:")
company1_dropdown = st.sidebar.selectbox('Select company 1',tickers)

company_id1 = company1_dropdown

company2_dropdown = st.sidebar.selectbox(
        'Select company 2',tickers
)

company_id2 = company2_dropdown
if pd.isnull(industry_dropdown):
        table1 = df.loc[(df['ticker_name'] == company_id1) ]
else:
        table1 = df.loc[(df['ticker_name'] == company_id1) &  (df['industry_group'] == industry_dropdown)]
if pd.isnull(industry_dropdown):
        table2 = df.loc[(df['ticker_name'] == company_id2) ]
else:
        table2 = df.loc[(df['ticker_name'] == company_id2) &  (df['industry_group'] == industry_dropdown)]
#show company  1 & 2 table
st.write(str(company_id1),'\n',table1.head())
if company_id1 != company_id2:
        st.write(str(company_id2),'\n',table2.head())



#dataframe for plotting
company_lst = [company_id1,company_id2]
compare_df = df.loc[df['ticker_name'].isin(company_lst)]

reshaped_df = pd.melt(compare_df, id_vars=["ticker_name","industry_group"], var_name="year")
#df_re = reshaped_df.pivot(index='year', columns='ticker_name', values='value')


sns.catplot(x = "year",y = "value",hue = "ticker_name",data = reshaped_df,kind = "bar")
plt.xlabel('Year')
plt.ylabel('Revenue (Millions $)')
plt.show()
st.set_option('deprecation.showPyplotGlobalUse', False)
st.pyplot()



#tbl1_rev = table1_t['Total Revenue'][1:4].to_list()
#tbl2_rev = table2_t['Total Revenue'][1:4].to_list()


#stock price
st.write(""""
# Stock Price

Shown are stock closing price and volume of
        """,company_id1)

tickSymb_company1 = company_id1

tickSymb_company2 = company_id2

tickerData_company1 = yf.Ticker(tickSymb_company1)

if company_id1 != company_id2:
        tickerData_company2 = yf.Ticker(tickSymb_company2)


tickerDF_company1 = tickerData_company1.history(period = 'id',start = '2014-5-31',end = '2017-5-31')

if company_id1 != company_id2:
        tickerDF_company2 = tickerData_company2.history(period = 'id',start = '2014-5-31',end = '2017-5-31')

#line chart company 1
if tickerDF_company1.Close.empty == True:
        st.write("No data available at the moment")
else:
        st.line_chart(tickerDF_company1.Close)
st.write("")
if tickerDF_company1.Volume.empty == True:
        st.line_chart("No data available at the moment")
else:
        st.line_chart(tickerDF_company1.Volume)
        
if company_id1 != company_id2:
        st.write("# Stock Price")

        st.write("Shown are stock closing price and volume of",company_id2)


#line chart company 2
if company_id1 != company_id2:
        if tickerDF_company2.Close.empty == True:
                st.write("No data available at the moment")
        else:
                st.line_chart(tickerDF_company2.Close)
st.write("")

if company_id1 != company_id2:
        if tickerDF_company2.Volume.empty == True:
                st.line_chart("No data available at the moment")
        else:
                st.line_chart(tickerDF_company2.Volume)

 
