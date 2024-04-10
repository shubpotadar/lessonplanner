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
        st.session_state.response = response
        st.experimental_rerun()
        # st.experimental_show()

    # Displaying response page
    if "response" in st.session_state:
        display_response(st.session_state.response)

# Function to display response page with table
def display_response(response):
    st.header("Generated Plan")
    st.write("Below is the response from Mistral model:")
    topics = response.split('\n')
    data = []
    for i, topic in enumerate(topics, 1):
        topic = topic.strip().replace("*", "")
        if topic.strip():
         data.append({"Topic": topic.strip(), "Website Link": "https://example.com"})  # Dummy link for now
    st.table(data)

if __name__ == "__main__":
    main()
