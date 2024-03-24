import streamlit as st
import time

st.title("Stock Market Calculator")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("styles.css")

# this is the main code to get the calc to work and the results to show
def price_calculation():
    global market_cap, supply

    result=(market_cap)/(supply)
    result=round(result,2)
    st.write(f"${result} USD")

market_cap=st.number_input("What is the Market Cap?")
supply=st.number_input("What is the Circulating Supply?")

x=st.button("Ready to Calculate?")

if x:
    price_calculation()
else:
    time.sleep(10)
    st.rerun()

# this is the main code for market cap calc
def market_calculation():
    global price, supply
    result=(supply)*(price)
    result=round(result,2)
    st.write(f"${result} USD")

price=st.number_input("What is the Price?")

y=st.button("Ready to Calculate?")

if y:
    market_calculation()
else:
    time.sleep(10)
    st.rerun()

