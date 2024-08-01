import json
import os
from dotenv import load_dotenv
load_dotenv()
import openai

def voice_bundle_tariff(country):
    tariffs = {
        "CountryA": {"tariff": 0.5, "currency": "USD", "unit": "minute"},
        "CountryB": {"tariff": 0.2, "currency": "USD", "unit": "minute"},
        "CountryC": {"tariff": 0.3, "currency": "USD", "unit": "minute"}
    }
    return json.dumps(tariffs.get(country, {}))

def data_bundle_tariff(country):
    tariffs = {
        "CountryA": {"tariff": 0.8, "currency": "USD", "unit": "megabytes"},
        "CountryB": {"tariff": 0.9, "currency": "USD", "unit": "megabytes"},
        "CountryC": {"tariff": 5.0, "currency": "USD", "unit": "megabytes"}
    }
    return json.dumps(tariffs.get(country, {}))


api_key = os.getenv('OPENAI_API_KEY')

conversation_history = []

def add_to_history(role, content):
    conversation_history.append({"role": role, "content": content})

def generate_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=conversation_history + [{"role": "user", "content": prompt}],
        max_tokens=150
    )
    message = response['choices'][0]['message']['content']
    add_to_history("assistant", message)
    return message

def few_shot_prompt(prompt):
    examples = [
        {"role": "system", "content": "You are a helpful assistant who always includes a joke in the response."},
        {"role": "user", "content": "Tell me about the weather."},
        {"role": "assistant", "content": "The weather is sunny. Why don't scientists trust atoms? Because they make up everything!"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=examples + [{"role": "user", "content": prompt}],
        max_tokens=150
    )
    return response['choices'][0]['message']['content']

def handle_function_call(function_name, argument):
    if function_name == "data_bundle_tariff":
        return data_bundle_tariff(argument)
    elif function_name == "voice_bundle_tariff":
        return voice_bundle_tariff(argument)
    else:
        return json.dumps({"error": "Function not found"})
