import streamlit as st
import math
import numpy as np
import matplotlib.pyplot as plt

# Streamlit interface for arithmetic operations
def arithmetic_operations():
    st.write("## Arithmetic Operations")
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    
    st.write(f"The result of {num1} {operation} {num2} is {result}")

# Streamlit interface for trigonometric operations
def trigonometric_operations():
    st.write("## Trigonometric Operations")
    angle = st.number_input("Enter angle in degrees", value=0.0)
    radian = math.radians(angle)
    operation = st.selectbox("Choose operation", ["sin", "cos", "tan"])
    
    if operation == 'sin':
        result = math.sin(radian)
    elif operation == 'cos':
        result = math.cos(radian)
    elif operation == 'tan':
        result = math.tan(radian)
    
    st.write(f"The result of {operation}({angle}°) is {result}")

# Streamlit interface to plot a graph
def plot_graph():
    st.write("## Plot Graph")
    func = st.selectbox("Choose function", ["sin", "cos", "tan"])
    x = np.linspace(0, 2 * np.pi, 100)
    
    if func == 'sin':
        y = np.sin(x)
    elif func == 'cos':
        y = np.cos(x)
    elif func == 'tan':
        y = np.tan(x)
    
    plt.plot(x, y)
    plt.title(f'Plot of {func}(x)')
    plt.xlabel('x')
    plt.ylabel(f'{func}(x)')
    plt.grid(True)
    st.pyplot(plt)

# Streamlit app layout
st.title("Scientific and Graphical Calculator")
mode = st.sidebar.selectbox("Choose mode", ["Arithmetic", "Trigonometric", "Plot Graph"])

if mode == "Arithmetic":
    arithmetic_operations()
elif mode == "Trigonometric":
    trigonometric_operations()
elif mode == "Plot Graph":
    plot_graph()
