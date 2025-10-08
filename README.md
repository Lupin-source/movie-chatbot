# Movie Recommendation Chatbot

A rule-based chatbot that recommends movies based on user preferences using predefined rules and a modern web interface inspired by Instagram messaging.

## Features

- **Rule-Based AI**: Decision-making guided by logical conditions (if-elif-else) rather than machine learning.
- **Modern Web UI**: Messaging interface inspired by Instagram, with chat bubbles and responsive design.
- **Keyword Detection**: Recognizes genres (action, romance, comedy, horror, drama), moods (happy, sad, thrilling, scary, romantic), and intents (recommend, suggest).
- **Predefined Movie Database**: Categorized recommendations for quick responses.
- **Interactive Conversation**: Handles greetings, recommendations, and exit commands.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/Lupin-source/movie-chatbot.git
   cd movie-chatbot
   ```

2. Install dependencies:
   ```
   pip install flask
   ```

3. Run the application:
   ```
   python app.py
   ```

4. Open your browser and navigate to `http://localhost:5000`.

## Usage

- Start chatting by typing messages such as:
  - "recommend an action movie"
  - "I'm feeling romantic"
  - "suggest something happy"
- Type "exit" to quit the conversation.

## Project Structure

- `app.py`: Flask backend with chatbot logic.
- `templates/index.html`: Frontend UI.
- `movie_chatbot.py`: Original Tkinter version (optional).
- `.gitignore`: Ignores Python cache files.

## Technologies Used

- Python
- Flask
- HTML/CSS/JavaScript

## Contributing

Feel free to fork the repository and submit pull requests for improvements.

## License

MIT License