# Mnemosyne-o1-hackathon-

Functional requirements: From my view they are as follows:
1 - UI to turn voice into LLM command (User - "Tell me a story at first year reading level."
2 - Voice to record the user speech as they read aloud the story.
3 - The LLM must determine the reading level of the user based on their speech.
4 - The LLM must then adjust the complexity of the story it generates in real time to match the users reading level.
5 - This app must store the user information at the end of every usage so that the user can start at the same place they stopped.

### README.md

# Mnemosyne-o1-hackathon

This project is designed for the lablab.ai o1 hackathon (27-29SEPT2024). It captures user speech, determines their reading level, and generates stories appropriate for their reading level. User progress is saved and loaded to ensure continuity between sessions.

## Features
1. **Voice Command Interface**: Converts voice inputs into text commands.
2. **Speech Recording**: Records user speech as they read aloud.
3. **Reading Level Assessment**: Determines the user's reading level based on their speech.
4. **Story Generation**: Adjusts the complexity of generated stories in real-time to match the user's reading level.
5. **User Progress Storage**: Saves user progress to continue from the last session.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/AdvancedHueristics/Mnemosyne-o1-hackathon-.git
   cd Mnemosyne-o1-hackathon-
   ```

2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```sh
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory and add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key
     ```

## Usage

1. Run the application:
   ```sh
   python app.py
   ```

2. Follow the prompts to speak and interact with the application.

## Main Components

- **capture_speech()**: Captures and converts speech to text.
- **determine_reading_level(text)**: Determines the reading level of the user based on their speech text.
- **generate_story(client, reading_level)**: Generates a story based on the user's reading level.
- **save_progress(user_data)**: Saves user progress to a JSON file.
- **load_progress()**: Loads user progress from a JSON file.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License.

---

This README provides a high-level overview of the project, installation instructions, usage guidelines, and information about the main components. Feel free to customize it further based on your specific needs.
