import tkinter as tk
from tkinter import messagebox
import random

class OneATwoBGame:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("1A2B Game")

        self.secret_number = self.generate_secret_number()

        tk.Label(self.root, text="Guess the 4-digit number:").pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        tk.Button(self.root, text="Guess", command=self.check_guess).pack()
        tk.Button(self.root, text="Reveal Answer", command=self.reveal_answer).pack()

        self.rounds_text = tk.Text(self.root, height=10, width=50)
        self.rounds_text.pack()

    def generate_secret_number(self):
        return ''.join(random.sample('0123456789', 4))

    def check_guess(self):
        guess = self.entry.get()
        if len(guess) != 4 or not guess.isdigit():
            messagebox.showerror("Error", "Please enter a 4-digit number.")
            return
        
        num_correct = sum(guess[i] == self.secret_number[i] for i in range(4))
        num_incorrect = sum(guess[i] in self.secret_number for i in range(4)) - num_correct
        
        self.rounds_text.insert(tk.END, f"Guess: {guess}, Result: {num_correct}A{num_incorrect}B\n")
        self.entry.delete(0, tk.END)
        
        if guess == self.secret_number:
            messagebox.showinfo("Congratulations", "You've guessed the correct number!")
            self.root.quit()
    
    def reveal_answer(self):
        messagebox.showinfo("Answer", f"The correct number is: {self.secret_number}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = OneATwoBGame()
    game.run()
