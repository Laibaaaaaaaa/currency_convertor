# Importing necessary libraries
import streamlit as st
from forex_python.converter import CurrencyRates

# Initialize the currency converter
c = CurrencyRates()

# Streamlit app title
st.title("Currency Converter")

# Input fields for amount and currencies
amount = st.number_input("Enter the amount", min_value=0.0, value=1.0)
from_currency = st.text_input("Currency to convert from (e.g., 'USD')", "USD").upper()
to_currency = st.text_input("Currency to convert to (e.g., 'EUR')", "EUR").upper()

# Conversion logic and display of result
if st.button("Convert"):
    try:
        conversion_rate = c.get_rate(from_currency, to_currency)
        converted_amount = amount * conversion_rate
        st.success(f"{amount} {from_currency} = {converted_amount:.2f} {to_currency}")
    except Exception as e:
        st.error(f"Error: {e}")
