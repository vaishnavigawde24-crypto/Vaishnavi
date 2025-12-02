import streamlit as st
import math
import numpy as np

# Page configuration
st.set_page_config(page_title="Scientific Calculator", page_icon="🔢", layout="centered")

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 8px;
        margin: 2px;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'memory' not in st.session_state:
    st.session_state.memory = 0

st.title("🔢 Scientific Calculator")

# Display
display_container = st.container()
with display_container:
    st.markdown(f"### Display: `{st.session_state.display}`")

# Function to update display
def update_display(value):
    if st.session_state.display == "0" or st.session_state.display == "Error":
        st.session_state.display = str(value)
    else:
        st.session_state.display += str(value)

def clear_display():
    st.session_state.display = "0"

def calculate():
    try:
        # Replace mathematical functions for evaluation
        expression = st.session_state.display
        expression = expression.replace('×', '*').replace('÷', '/')
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        
        # Evaluate the expression
        result = eval(expression, {"__builtins__": None}, {
            "sin": math.sin, "cos": math.cos, "tan": math.tan,
            "asin": math.asin, "acos": math.acos, "atan": math.atan,
            "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
            "log": math.log10, "ln": math.log, "log10": math.log10,
            "sqrt": math.sqrt, "exp": math.exp, "pow": pow,
            "pi": math.pi, "e": math.e, "abs": abs,
            "factorial": math.factorial, "degrees": math.degrees,
            "radians": math.radians
        })
        st.session_state.display = str(result)
    except:
        st.session_state.display = "Error"

def backspace():
    if len(st.session_state.display) > 1:
        st.session_state.display = st.session_state.display[:-1]
    else:
        st.session_state.display = "0"

def add_function(func):
    if st.session_state.display == "0":
        st.session_state.display = func + "("
    else:
        st.session_state.display += func + "("

# Calculator buttons layout
col1, col2, col3, col4, col5 = st.columns(5)

# Row 1 - Memory and Clear functions
with col1:
    if st.button("MC"):
        st.session_state.memory = 0
with col2:
    if st.button("MR"):
        st.session_state.display = str(st.session_state.memory)
with col3:
    if st.button("M+"):
        try:
            st.session_state.memory += float(eval(st.session_state.display))
        except:
            pass
with col4:
    if st.button("C"):
        clear_display()
with col5:
    if st.button("⌫"):
        backspace()

st.divider()

# Row 2 - Trigonometric functions
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("sin"):
        add_function("sin")
with col2:
    if st.button("cos"):
        add_function("cos")
with col3:
    if st.button("tan"):
        add_function("tan")
with col4:
    if st.button("π"):
        update_display("π")
with col5:
    if st.button("e"):
        update_display("e")

# Row 3 - Advanced functions
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("√"):
        add_function("sqrt")
with col2:
    if st.button("x²"):
        st.session_state.display += "**2"
with col3:
    if st.button("xʸ"):
        st.session_state.display += "**"
with col4:
    if st.button("log"):
        add_function("log")
with col5:
    if st.button("ln"):
        add_function("ln")

# Row 4 - Numbers
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("7"):
        update_display("7")
with col2:
    if st.button("8"):
        update_display("8")
with col3:
    if st.button("9"):
        update_display("9")
with col4:
    if st.button("÷"):
        update_display("÷")
with col5:
    if st.button("("):
        update_display("(")

# Row 5
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("4"):
        update_display("4")
with col2:
    if st.button("5"):
        update_display("5")
with col3:
    if st.button("6"):
        update_display("6")
with col4:
    if st.button("×"):
        update_display("×")
with col5:
    if st.button(")"):
        update_display(")")

# Row 6
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("1"):
        update_display("1")
with col2:
    if st.button("2"):
        update_display("2")
with col3:
    if st.button("3"):
        update_display("3")
with col4:
    if st.button("-"):
        update_display("-")
with col5:
    if st.button("!"):
        add_function("factorial")

# Row 7
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    if st.button("0"):
        update_display("0")
with col2:
    if st.button("."):
        update_display(".")
with col3:
    if st.button("=", type="primary"):
        calculate()
with col4:
    if st.button("+"):
        update_display("+")
with col5:
    if st.button("|x|"):
        add_function("abs")

# Instructions
with st.expander("ℹ️ Instructions"):
    st.markdown("""
    **How to use:**
    - Click number buttons to input numbers
    - Use operation buttons (+, -, ×, ÷) for basic operations
    - Scientific functions: sin, cos, tan, log, ln, sqrt
    - Constants: π (pi), e (Euler's number)
    - Memory functions: MC (clear), MR (recall), M+ (add to memory)
    - Press = to calculate the result
    - Press C to clear, ⌫ to backspace
    
    **Note:** Trigonometric functions work with radians by default.
    """)

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
