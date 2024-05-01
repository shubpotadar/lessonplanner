import streamlit as st
from ollama import chat

# Function to get response from LLama 2 model
input_text = ""
with open("D:/projects/ashish/WebScraper/WebScraper/result_from_geeks_for_geeks.txt", "r", encoding='utf-8') as file:
    lines = file.readlines()
    for line in lines:
        line = line.strip()
        input_text += line

print(input_text)
def get_LLama_response(input_text):
    messages = [
        {
            'role': 'user',
            'content': f"summarize the follwoing content for revision and study into 200 words, include only the important parts for better understanding and manage all the cases of formatting.here is the input={input_text}",
        },
    ]
    response = chat('Mistral', messages=messages)
    return response['message']['content']


summarized_content = get_LLama_response(input_text)
print(summarized_content)

with open("D:/projects/ashish/lessonplanner-main/summarized_content.txt", "w", encoding='utf-8') as file:
    file.write(summarized_content)
