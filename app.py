import os
import json
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to capture and convert speech to text
def capture_speech():
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)
    try:
        user_content = recognizer.recognize_google(audio)
        print("You said: " + user_content)
        return user_content
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to determine reading level
def determine_reading_level(text):
    # Placeholder function to determine reading level
    # You can use more sophisticated methods or models to determine reading level
    if len(text.split()) < 50:
        return "beginner"
    elif len(text.split()) < 100:
        return "intermediate"
    else:
        return "advanced"

# Function to generate a story based on reading level
def generate_story(client, reading_level):
    prompt = f"Generate a {reading_level} level story for a user to read."
    response = client.chat.completions.create(
        model="o1-mini",
        messages=[
            {"role": "system", "content": prompt},
        ],
        max_tokens=2000,
    )
    story = response.choices[0].message.content
    print(f"Generated {reading_level} story:\n", story)
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

# Get the API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.aimlapi.com/",
)

# Load user progress
user_data = load_progress()
reading_level = user_data["reading_level"]
last_story = user_data["last_story"]

# Main loop to capture recitation and adjust story
while True:
    # If there is a last story, prompt the user to recite it
    if last_story:
        print("Please recite the last story to continue...")
        user_content = capture_speech()
        reading_level = determine_reading_level(user_content)
        print(f"Determined reading level: {reading_level}")
    
    # Generate and adjust story based on reading level
    story = generate_story(client, reading_level)
    
    # Wait for user to recite the story back
    print("Please recite the generated story back to adjust further...")
    user_content = capture_speech()
    
    # Save user progress
    user_data = {"reading_level": reading_level, "last_story": story}
    save_progress(user_data)
