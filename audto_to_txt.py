import streamlit as st
import plotly.graph_objects as go
from datetime import datetime
import calendar
import torch
import soundfile as sf
from transformers import pipeline
import os
import tempfile

# --------------- SETTINGS ------------------


incomes = ["Salary", "Blog", "Other Income"]
expenses = ["Rent", "Utilities", "Groceries", "Car"]
currency = "USD"
page_title = "Sample Audio to Text Converter"
page_icon = ":money_with_wings:"
layout = "centered"








# ------------------------------------------




st.set_page_config(page_title = page_title,
                    page_icon = page_icon,
                    layout = layout)

st.title(page_title + " " + page_icon)

# --- DROP DOWN VALUES FOR SELECTING PERIOD ---


import os

def find_file_path(file_name, start_dir="."):
    for root, dirs, files in os.walk(start_dir):
        if file_name in files:
            return os.path.join(root, file_name)

    # If the file is not found
    return None


# Load the automatic speech recognition (ASR) model
asr_model = pipeline("automatic-speech-recognition")

# Get the uploaded file
uploaded_file = st.file_uploader("Upload audio file:", type=["wav", "mp3"])

if uploaded_file is not None:

    # Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(uploaded_file.read())
        temp_file_path = temp_file.name

    transcribed_text = asr_model(temp_file_path)

    # Display the transcribed text
    st.text("Transcribed Text:")
    st.text(transcribed_text)
