import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    # Input for three numbers
    num1 = st.number_input("Enter the first number", value=0)
    num2 = st.number_input("Enter the second number", value=0)
    num3 = st.number_input("Enter the third number", value=0)

    # Button to calculate the largest number
    if st.button("Find Largest Number"):
        largest_number = find_largest_numb