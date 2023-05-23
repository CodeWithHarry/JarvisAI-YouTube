# Jarvis AI

Jarvis AI is a voice-controlled artificial intelligence assistant implemented in Python. It utilizes various libraries and APIs to perform tasks such as voice recognition, web browsing, text-to-speech, and communication with the OpenAI API for generating AI responses.

## Prerequisites

Make sure you have the following dependencies installed:

- `speech_recognition`
- `webbrowser`
- `openai`

You will also need an API key from OpenAI to access the language models.

## Usage

1. Clone the repository and navigate to the project directory.

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

3. Update the `apikey` in the `config.py` file with your OpenAI API key.

4. Run the `jarvis.py` script:

   ```shell
   python jarvis.py
   ```

5. Jarvis will start listening for voice commands. You can interact with it by speaking your queries or commands.

## Functionality

- **Chatting**: Jarvis uses the OpenAI chat model to generate responses to user queries or inputs. It maintains a conversation history and appends new queries to it.

- **AI Prompt**: You can provide a prompt to the AI model using the "Using artificial intelligence" command. It generates a response based on the prompt and saves the response in a text file.

- **Web Browsing**: Jarvis can open various websites such as YouTube, Wikipedia, and Google. Simply say "Open YouTube" or "Open Wikipedia" to launch the respective website.

- **Music Playback**: You can open a music file by saying "Open music". Make sure to update the `musicPath` variable in the code with the path to your music file.

- **Time**: Jarvis can tell you the current time upon request. Just say "What's the time?" or a similar phrase.

- **Application Launch**: Jarvis can open specific applications like FaceTime and Passky. Use commands like "Open FaceTime" or "Open Pass" to launch the applications.

- **Reset Chat**: You can reset the conversation history with Jarvis by saying "Reset chat".

- **Quit**: To exit Jarvis, say "Jarvis Quit".

## Contributions

Contributions to improve and enhance Jarvis AI are welcome. Feel free to fork the repository, make changes, and submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
