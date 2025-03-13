import json
import os

from slide_deck import SlideDeck
from llm_call import chat_completion_request

FOLDER = "generated"

if not os.path.exists(FOLDER):
    os.makedirs(FOLDER)

def generate_json_list_of_slides(content):
    try:
        resp = chat_completion_request(content)
        obj = json.loads(resp)
        return obj
    except Exception as e:
        raise e

def generate_presentation(content):
    deck = SlideDeck()
    slides_data = generate_json_list_of_slides(content)
    title_slide_data = slides_data[0]
    slides_data = slides_data[1:]
    return deck.create_presentation(title_slide_data, slides_data)

import traceback
import streamlit as st

from slide_gen import generate_presentation

def create_ui():
    st.write("""
# Gen Slides
### Generating powerpoint slides for your text
""")

    content = st.text_area(label="Enter your text:", height=400)
    try:
        if content:
            filename = generate_presentation(content)
            st.write(f"file {filename} is generated.")
    except Exception:
        st.write("Error in generating slides.")
        st.write(traceback.format_exc())

if __name__ == "__main__":
    create_ui()