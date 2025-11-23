import streamlit as st
import math

st.title("🧮 Scientific Calculator")

operation = st.selectbox(
    "Choose an operation:",
    [
        "Add", "Subtract", "Multiply", "Divide",
        "Power", "Square Root", "Sine", "Cosine",
        "Tangent", "Log10", "Natural Log", "Factorial"
    ]
)

if operation in ["Add", "Subtract", "Multiply", "Divide", "Power"]:
    a = st.number_input("Enter first number", value=0.0)
    b = st.number_input("Enter second number", value=0.0)

elif operation in ["Square Root", "Sine", "Cosine", "Tangent", "Log10", "Natural Log", "Factorial"]:
    a = st.number_input("Enter number", value=0.0)

if st.button("Calculate"):
    try:
        if operation == "Add":
            result = a + b
        elif operation == "Subtract":
