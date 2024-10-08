import os
import json
import streamlit as st
import speech_recognition as sr
import openai  # Import the OpenAI package
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Callback function for background listening
def callback(recognizer, audio):
    try:
        user_content = recognizer.recognize_google(audio)
        st.write(f"You said: {user_content}")
        st.session_state['user_content'] = user_content
    except sr.UnknownValueError:
        st.error("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        st.error(f"Could not request results from Google Speech Recognition service; {e}")

# Function to capture and convert speech to text (non-blocking)
def capture_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        st.info("Please say something...")
        recognizer.listen_in_background(source, callback)

# Function to determine reading level
def determine_reading_level(text):
    if len(text.split()) < 50:
        return "beginner"
    elif len(text.split()) < 100:
        return "intermediate"
    else:
        return "advanced"

# Function to generate a story based on reading level
def generate_story(reading_level):
    prompt = f"Generate a {reading_level} level story for a user to read."
    
    # Use the o1-mini model as per your requirement
    response = openai.ChatCompletion.create(
        model="o1-mini",  # Keep using o1-mini as the model
        messages=[
            {"role": "system", "content": prompt},
        ],
        max_tokens=2000,
    )
    story = response['choices'][0]['message']['content']
    st.write(f"Generated {reading_level} story:\n{story}")
    return story

# Function to save user progress
def save_progress(user_data):
    with open("user_progress.json", "w") as file:
        json.dump(user_data, file)

# Function to load user progress
def load_progress():
    if os.path.exists("user_progress.json"):
        with open("user_progress.json", "r") as file:
            return json.load(file)
    return {"reading_level": "beginner", "last_story": ""}

# Get API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")

# Set API key for OpenAI
openai.api_key = api_key

# Load user progress
user_data = load_progress()
reading_level = user_data["reading_level"]
last_story = user_data["last_story"]

# Streamlit UI
st.title("Speech-to-Story App")

if 'user_content' not in st.session_state:
    st.session_state['user_content'] = ""

if last_story:
    st.write("Please recite the last story to continue...")
    if st.button("Start Listening", on_click=capture_speech, key="listen_story"):
        if st.session_state['user_content']:
            reading_level = determine_reading_level(st.session_state['user_content'])
            st.write(f"Determined reading level: {reading_level}")

if st.button("Generate Story", key="generate_story"):
    story = generate_story(reading_level)
    last_story = story

if last_story:
    st.write("Please recite the generated story back to adjust further...")
    if st.button("Start Listening", on_click=capture_speech, key="listen_generated_story"):
        if st.session_state['user_content']:
            reading_level = determine_reading_level(st.session_state['user_content'])
            st.write(f"New determined reading level: {reading_level}")

# Save user progress
user_data = {"reading_level": reading_level, "last_story": last_story}
save_progress(user_data)
