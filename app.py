from flask import Flask, render_template, request, jsonify
import random

# Movie database
movies = {
    "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
    "romance": ["The Notebook", "Pride and Prejudice", "La La Land"],
    "comedy": ["The Grand Budapest Hotel", "Superbad", "Groundhog Day"],
    "horror": ["The Conjuring", "Hereditary", "Get Out"],
    "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"]
}

# Keyword detection
def detect_keywords(user_input):
    input_lower = user_input.lower()
    genres = ["action", "romance", "comedy", "horror", "drama"]
    moods = {"happy": "comedy", "sad": "drama", "thrilling": "action", "scary": "horror", "romantic": "romance"}
    intents = ["recommend", "suggest", "movie"]

    detected_genre = None
    detected_mood = None
    detected_intent = False

    for genre in genres:
        if genre in input_lower:
            detected_genre = genre
            break

    for mood, genre in moods.items():
        if mood in input_lower:
            detected_mood = genre
            break

    for intent in intents:
        if intent in input_lower:
            detected_intent = True
            break

    return detected_genre, detected_mood, detected_intent

# Response logic
def get_response(detected_genre, detected_mood, detected_intent, user_input):
    if detected_intent:
        if detected_genre:
            movie = random.choice(movies[detected_genre])
            return f"I recommend '{movie}' from the {detected_genre} genre!"
        elif detected_mood:
            movie = random.choice(movies[detected_mood])
            return f"Based on your mood, I suggest '{movie}'!"
        else:
            return "What genre or mood are you in the mood for? Like action, romance, comedy, horror, or drama?"
    else:
        if detected_genre or detected_mood:
            genre = detected_genre or detected_mood
            movie = random.choice(movies[genre])
            return f"Sounds like you're interested in {genre}. How about '{movie}'?"
        else:
            return "I'm not sure what you're looking for. Try mentioning a genre like action or romance, or say 'recommend a movie'!"

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input.lower() == 'exit':
        return jsonify({'response': 'Goodbye!'})
    detected_genre, detected_mood, detected_intent = detect_keywords(user_input)
    response = get_response(detected_genre, detected_mood, detected_intent, user_input)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)