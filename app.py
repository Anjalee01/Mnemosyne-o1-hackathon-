import os
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

# Get the API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.aimlapi.com/",
)

# Main loop to capture recitation and adjust story
while True:
    # Capture user's recitation
    user_content = capture_speech()
    
    # Determine reading level
    reading_level = determine_reading_level(user_content)
    print(f"Determined reading level: {reading_level}")
    
    # Generate and adjust story based on reading level
    story = generate_story(client, reading_level)
    
    # Wait for user to recite the generated story back to adjust further...
    print("Please recite the generated story back to adjust further...")
    user_content = capture_speech()
