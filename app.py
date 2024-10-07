import os
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the source for input
with sr.Microphone() as source:
    print("Please say something...")
    audio = recognizer.listen(source)

# Convert speech to text
try:
    user_content = recognizer.recognize_google(audio)
    print("You said: " + user_content)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
    user_content = ""
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    user_content = ""

# Get the API key from environment variables
api_key = os.environ.get("OPENAI_API_KEY")

# Initialize the OpenAI client
client = OpenAI(
    api_key=api_key,
    base_url="https://api.aimlapi.com/",
)

# Create a chat completion
chat_completion = client.chat.completions.create(
    model="o1-mini",
    messages=[
        {"role": "user", "content": user_content},
    ],
    max_tokens=2000,
)

# Get the response and print it
response = chat_completion.choices[0].message.content
print("Response:\n", response)
