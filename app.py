import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))
def predict_forest(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6):
    input=np.array([[LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6]]).astype(np.float64)
    prediction=model.predict(input)
    return prediction

def main():
    st.title("Streamlit Tutorial")
    html_temp = """
    <div style="background-color:#025246 ;padding:10px">
    <h2 style="color:white;text-align:center;">Forest Fire Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    LIMIT_BAL = st.text_input("Limit_bal","Type Here")
    EDUCATION = st.text_input("Education","Type Here")
    MARRIAGE = st.text_input("Marraige","Type Here")
    AGE = st.text_input("Age","Type Here")
    PAY_1 = st.text_input("Pay_1","Type Here")
    BILL_AMT1 = st.text_input("Bill_amt1","Type Here")
    BILL_AMT2 = st.text_input("Bill_amt2","Type Here")
    BILL_AMT3 = st.text_input("Bill_amt3","Type Here")
    BILL_AMT4 = st.text_input("Bill_amt4","Type Here")
    BILL_AMT5 = st.text_input("Bill_amt5","Type Here")
    BILL_AMT6 = st.text_input("Bill_amt6","Type Here")
    PAY_AMT1  = st.text_input("Pay_amt1","Type Here")
    PAY_AMT2  = st.text_input("Pay_amt2","Type Here")
    PAY_AMT3  = st.text_input("Pay_amt3","Type Here")
    PAY_AMT4  = st.text_input("Pay_amt4","Type Here")
    PAY_AMT5  = st.text_input("Pay_amt5","Type Here")
    PAY_AMT6  = st.text_input("Pay_amt6","Type Here")



#     safe_html="""
#       <div style="background-color:#F4D03F;padding:10px >
#        <h2 style="color:white;text-align:center;"> Your forest is safe</h2>
#        </div>
#     """
#     danger_html="""
#       <div style="background-color:#F08080;padding:10px >
#        <h2 style="color:black ;text-align:center;"> Your forest is in danger</h2>
#        </div>
#     """

    if st.button("Predict"):
        output=predict_forest(LIMIT_BAL,EDUCATION,MARRIAGE,AGE,PAY_1,BILL_AMT1,BILL_AMT2,BILL_AMT3,BILL_AMT4,BILL_AMT5,BILL_AMT6,PAY_AMT1,PAY_AMT2,PAY_AMT3,PAY_AMT4,PAY_AMT5,PAY_AMT6)
        st.success('The probability of fire taking place is {}'.format(output))

#         if output > 0.5:
#             st.markdown(danger_html,unsafe_allow_html=True)
#         else:
#             st.markdown(safe_html,unsafe_allow_html=True)

if __name__=='__main__':
    main()
