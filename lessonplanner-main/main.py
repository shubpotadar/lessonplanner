import streamlit as st
from ollama import chat

# Function to get response from LLama 2 model
def get_LLama_response(input_text, no_hours, level):
    messages = [
        {
            'role': 'user',
            'content': f"Generate a lesson plan for {no_hours} hours on {input_text} with a difficulty level of {level}. "
        },
    ]
    response = chat('lessonPlanner', messages=messages)
    return response['message']['content']

# Function to save response to a text file
def save_response_to_file(response):
    with open("generated_plan.txt", "w") as file:
        file.write(response)

# Streamlit UI
def main():
    st.set_page_config(page_title="Generate plan",
                       page_icon='🤖',
                       layout='centered',
                       initial_sidebar_state='collapsed')

    st.header("Generate plan 🤖")

    input_text = st.text_input("Enter the Topic")

    # creating to more columns for additional 2 fields

    col1, col2 = st.columns([8, 8])

    with col1:
        no_hours = st.text_input('No of hours')
    with col2:
        level = st.selectbox('Difficulty level',
                             ('beginner', 'intermediate', 'advanced'), index=0)

    submit = st.button("Generate")

    # Handling routing to response page
    if submit:
        response = get_LLama_response(input_text, no_hours, level)
        save_response_to_file(response)  # Save response to file
        st.session_state.response = response
        st.experimental_rerun()

    # Displaying response page
    if "response" in st.session_state:
        display_response(st.session_state.response)

# Function to display response page with table
import sys
sys.path.append(r'C:/Users/aharakun/Downloads/lessonplanner-main/WebScraper/WebScraper')
import fetch_url
from fetch_url import fetch_links

def display_response(response):
    st.header("Generated Plan")
    st.write("Below is the response from Mistral model:")
    topics = response.split('\n')
    data = []
    for i, topic in enumerate(topics, 1):
        topic = topic.strip().replace("*", "")
        if topic.strip():
            # Dummy link for now
            link=fetch_links(topic.strip())
            data.append({"Topic": topic.strip(),
                        "GFG Link": link[0],
                        "Javatpoint Link": link[1]})
    st.table(data)
    return response  # Return the response instead of displaying it directly


if __name__ == "__main__":
    main()
