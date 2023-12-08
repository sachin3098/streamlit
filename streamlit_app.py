import streamlit as st

def find_largest_number(num1, num2, num3):
    # Find the largest number among the three
    largest_number = max(num1, num2, num3)
    return largest_number

def main():
    st.title("Find the Largest Number App")

    # Input three numbers
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")

    # Display the input numbers
    st.write("You entered the numbers:")
    st.write("Number 1:", num1)
    st.write("Number 2:", num2)
    st.write("Number 3:", num3)

    # Find and display the largest number
    largest_number = find_largest_number(num1, num2, num3)
    st.write("The largest number is:", largest_number)

if __name__ == "__main__":
    main()
