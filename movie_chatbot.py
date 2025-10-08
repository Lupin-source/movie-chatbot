import random
import tkinter as tk
from tkinter import scrolledtext, END

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

class ChatbotGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Movie Recommendation Chatbot")
        self.root.geometry("500x600")

        # Chat history
        self.chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', height=20)
        self.chat_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Input frame
        input_frame = tk.Frame(root)
        input_frame.pack(fill=tk.X, padx=10, pady=5)

        self.input_entry = tk.Entry(input_frame, font=("Arial", 12))
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.input_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=(5,0))

        # Initial greeting
        self.add_message("Chatbot: Hello! I'm your movie recommendation chatbot. Type 'exit' to quit.")

    def add_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(END, message + "\n")
        self.chat_area.config(state='disabled')
        self.chat_area.see(END)

    def send_message(self, event=None):
        user_input = self.input_entry.get().strip()
        if not user_input:
            return
        self.input_entry.delete(0, END)
        self.add_message(f"You: {user_input}")

        if user_input.lower() == 'exit':
            self.add_message("Chatbot: Goodbye!")
            self.root.quit()
            return

        detected_genre, detected_mood, detected_intent = detect_keywords(user_input)
        response = get_response(detected_genre, detected_mood, detected_intent, user_input)
        self.add_message(f"Chatbot: {response}")

def main():
    root = tk.Tk()
    gui = ChatbotGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()