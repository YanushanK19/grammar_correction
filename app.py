# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1V-_FD6eoshaBM-aF8M4ittIy13969Vy-
"""

import streamlit as st
import stanza

# Import the grammar correction function
from grammar_correction import process_tamil_text_with_correction

# Initialize Stanza pipeline for Tamil
@st.cache_resource
def load_pipeline():
    return stanza.Pipeline(lang='ta', processors='tokenize,pos')

pipeline = load_pipeline()

# Streamlit App
st.title("Tamil Grammar Correction Tool")
st.write("Enter a Tamil sentence below to check and correct grammatical errors.")

# Input text box
input_text = st.text_area("Input Tamil Text", height=150)

if st.button("Correct Grammar"):
    if input_text.strip():
        corrected_text, errors = process_tamil_text_with_correction(pipeline, input_text)

        st.subheader("Corrected Text")
        st.write(corrected_text)

        if errors:
            st.subheader("Detected Errors")
            for error in errors:
                st.error(error)
        else:
            st.success("No grammatical errors detected!")
    else:
        st.warning("Please enter some Tamil text to process.")