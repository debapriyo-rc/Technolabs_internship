import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
def predict_forest(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6):
    input=np.array([[LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]]).astype(np.float64)
    prediction=model.predict(input)
    return prediction

def main():
    st.title("Streamlit")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Credit Card App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    LIMIT_BAL = st.text_input("Limit_bal")
    EDUCATION = st.text_input("Education")
    MARRIAGE = st.text_input("Marraige")
    AGE = st.text_input("Age")
    PAY_1 = st.text_input("Pay_1")
    BILL_AMT1 = st.text_input("Bill_amt1")
    BILL_AMT2 = st.text_input("Bill_amt2")
    BILL_AMT3 = st.text_input("Bill_amt3")
    BILL_AMT4 = st.text_input("Bill_amt4")
    BILL_AMT5 = st.text_input("Bill_amt5")
    BILL_AMT6 = st.text_input("Bill_amt6")
    PAY_AMT1  = st.text_input("Pay_amt1")
    PAY_AMT2  = st.text_input("Pay_amt2")
    PAY_AMT3  = st.text_input("Pay_amt3")
    PAY_AMT4  = st.text_input("Pay_amt4")
    PAY_AMT5  = st.text_input("Pay_amt5")
    PAY_AMT6  = st.text_input("Pay_amt6")


    if st.button("Predict"):
        output=predict_forest(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)
        st.success('The value is {}'.format(output))

if __name__=='__main__':
    main()
