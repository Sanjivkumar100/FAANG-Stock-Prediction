import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
st.title("FAANG Stock Prices")
st.markdown(
    """
    This application allows you to Predicts the stock prices of FAANG companies. The application is built using Streamlit and Python.
    In this application, you can select a company and input the stock prices to predict the stock price.
    """
)

def predict_price(company, Opening_Price, High_Price, Low_Price, Adj_Close, Volume):
    try:
        if company=='Apple':
            
            model = pickle.load(open('AppleModel.pkl', 'rb'))
            result = model.predict([[Opening_Price, High_Price, Low_Price, Adj_Close, Volume]])
            return result
        elif company=='Amazon':
           
            model = pickle.load(open('AmazonModel.pkl', 'rb'))
            result = model.predict([[Opening_Price, High_Price, Low_Price, Adj_Close, Volume]])
            return result
        elif company=='Facebook':
            model = pickle.load(open('FacebookModel.pkl', 'rb'))
            result = model.predict([[Opening_Price, High_Price, Low_Price, Adj_Close, Volume]])
            return result
        elif company=='Google':
           
            model = pickle.load(open('GoogleModel.pkl', 'rb'))
            result = model.predict([[Opening_Price, High_Price, Low_Price, Adj_Close, Volume]])
            return result
        elif company=='Netflix':
           
            model = pickle.load(open('NetflixModel.pkl', 'rb'))
            result = model.predict([[Opening_Price, High_Price, Low_Price, Adj_Close, Volume]])
            return result
        else:
            return "Select a Company"
    except Exception as e:
        return "Error: {}".format(e)

try:
    with st.form(key='Stock Form'):
        company = st.selectbox("Company", ['Apple', 'Amazon', 'Facebook', 'Google', 'Netflix'])
        if  company:
            Opening_Price = st.number_input("Opening Price", min_value=0.0, max_value=10000.0, value=0.0)
            High_Price = st.number_input("High Price", min_value=0.0, max_value=10000.0, value=0.0)
            Low_Price = st.number_input("Low Price", min_value=0.0, max_value=10000.0, value=0.0)
            Adj_Close = st.number_input("Adj Close", min_value=0.0, max_value=10000.0, value=0.0)
            Volume = st.number_input("Volume", min_value=0, max_value=1000000000, value=0)
            predict=st.form_submit_button("Predict")
            if predict:
                result = predict_price(company, Opening_Price, High_Price, Low_Price, Adj_Close, Volume)
                if isinstance(result, str):
                    st.error(result)
                else:
                    st.write(f"The predicted stock price for {company} is {result[0]:.2f}")
                    history = pd.read_csv(f'{company}.csv')
                    fig,ax=plt.subplots(figsize=(20, 10))  
                    ax.plot(history['date'], history['close'], label='Actual Price')
                    ax.axhline(y=result[0], color='r', linestyle='--', label='Predicted Price')
                    ax.set_xlabel('Date')
                    ax.set_ylabel('Price')
                    ax.set_title(f'{company} Stock Prices')

                    st.pyplot(fig)

               
                
except Exception as e:
    st.error(f"Error: {e}")
