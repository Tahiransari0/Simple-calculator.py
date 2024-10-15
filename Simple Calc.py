import streamlit as st

# Simple Calculator Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Streamlit UI Elements
st.title("Simple Calculator")

# Dropdown for selecting operation
operation = st.selectbox("Choose an operation", ["Add", "Subtract", "Multiply", "Divide"])

# Input fields for the two numbers
num1 = st.number_input("Enter first number", format="%f")
num2 = st.number_input("Enter second number", format="%f")

# Perform the selected operation
if st.button("Calculate"):
    if operation == "Add":
        result = add(num1, num2)
    elif operation == "Subtract":
        result = subtract(num1, num2)
    elif operation == "Multiply":
        result = multiply(num1, num2)
    elif operation == "Divide":
        result = divide(num1, num2)

    # Display the result
    st.write(f"The result is: {result}")
