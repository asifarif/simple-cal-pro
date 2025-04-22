# app.py
import streamlit as st

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

st.title("Simple Calculator")

operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

num1 = st.number_input("Enter first number:", format="%.2f")
num2 = st.number_input("Enter second number:", format="%.2f")

if st.button("Calculate"):
    if operation == "Add":
        st.write(f"The result is: {add(num1, num2)}")
    elif operation == "Subtract":
        st.write(f"The result is: {subtract(num1, num2)}")
    elif operation == "Multiply":
        st.write(f"The result is: {multiply(num1, num2)}")
    elif operation == "Divide":
        st.write(f"The result is: {divide(num1, num2)}")