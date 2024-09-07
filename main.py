import tkinter as tk
from tkinter import messagebox
import random

class JokeGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Joke Generator")

        # Sample jokes and their ratings
        self.jokes = [
            {"text": "Why don't scientists trust atoms? Because they make up everything!", "ratings": []},
            {"text": "What do you call fake spaghetti? An impasta!", "ratings": []},
            {"text": "Why did the scarecrow win an award? Because he was outstanding in his field!", "ratings": []},
            {"text": "How does a penguin build its house? Igloos it together!", "ratings": []},
            {"text": "What do you call cheese that isn't yours? Nacho cheese!", "ratings": []}
        ]

        self.current_joke = None

        # Create and place widgets
        self.create_widgets()

    def create_widgets(self):
        # Button to generate a joke
        self.generate_button = tk.Button(self.root, text="Tell me a joke", command=self.show_joke)
        self.generate_button.pack(pady=10)

        # Label to display the joke
        self.joke_label = tk.Label(self.root, text="", wraplength=300)
        self.joke_label.pack(pady=10)

        # Rating buttons
        self.rating_frame = tk.Frame(self.root)
        self.rating_frame.pack(pady=10)

        self.rating_buttons = [tk.Button(self.rating_frame, text=str(i), command=lambda i=i: self.rate_joke(i)) for i in range(1, 6)]
        for button in self.rating_buttons:
            button.pack(side=tk.LEFT)

        # Label to display average rating
        self.rating_label = tk.Label(self.root, text="")
        self.rating_label.pack(pady=10)

    def show_joke(self):
        self.current_joke = random.choice(self.jokes)
        self.joke_label.config(text=self.current_joke["text"])
        self.update_rating_label()

    def rate_joke(self, rating):
        if self.current_joke:
            self.current_joke["ratings"].append(rating)
            self.update_rating_label()
        else:
            messagebox.showwarning("Warning", "No joke to rate.")

    def update_rating_label(self):
        if self.current_joke and self.current_joke["ratings"]:
            avg_rating = sum(self.current_joke["ratings"]) / len(self.current_joke["ratings"])
            self.rating_label.config(text=f"Average Rating: {avg_rating:.1f} stars")
        else:
            self.rating_label.config(text="Average Rating: Not rated yet")

if __name__ == "__main__":
    root = tk.Tk()
    app = JokeGenerator(root)
    root.mainloop()

