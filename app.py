import streamlit as st
from methods import data_bundle_tariff, voice_bundle_tariff, generate_response, few_shot_prompt, handle_function_call
import openai
# Define the sections
st.title("AI BOT")

st.header("Tariff Methods")
country = st.selectbox("Select a country", ["CountryA", "CountryB", "CountryC"])
if st.button("Get Data Bundle Tariff"):
    result = data_bundle_tariff(country)
    st.json(result)

if st.button("Get Voice Bundle Tariff"):
    result = voice_bundle_tariff(country)
    st.json(result)

st.header("GPT-4 Model")
user_input = st.text_input("Enter your prompt")

if st.button("Generate Response"):
    response = generate_response(user_input)
    st.write(response)

if st.button("Generate a joke"):
    response = few_shot_prompt(user_input)
    st.write(response)

st.header("Function Calling")
function_name = st.selectbox("Select function to call", ["data_bundle_tariff", "voice_bundle_tariff"])
argument = st.text_input("Enter argument for the function")
if st.button("Call Function"):
    result = handle_function_call(function_name, argument)
    st.json(result)


