import tkinter as tk
from tkinter import messagebox
import random

# Constants
LOWER = 1
UPPER = 100
MAX_ATTEMPTS = 5

# Game Initialization
computer_guess = random.randint(LOWER, UPPER)
attempt_count = 0

# Game Function
def guess_number():
    global attempt_count
    user_input = guess_entry.get()
    try:
        user_guess = int(user_input)
        if LOWER <= user_guess <= UPPER:
            attempt_count += 1
            remaining_attempts = MAX_ATTEMPTS - attempt_count

            if user_guess == computer_guess:
                messagebox.showinfo('برنده شدید', 'هورااااا \n شما برنده شدید')
                # guess_button.config(state='disabled')  # Disable the button after a correct guess
                reset_game()
            elif user_guess < computer_guess:
                status_label.config(text='عدد بزرگتر را حدس بزنید\n'+'شما {} بار دیگر شانس مجدد دارید'.format(remaining_attempts))
            else:
                status_label.config(text='عدد کوچکتر را حدس بزنید\n'+'شما {} بار دیگر شانس مجدد دارید'.format(remaining_attempts))

            if remaining_attempts == 0:
                messagebox.showinfo('باختید', 'متاسفانه شما باختید'+'! '+'عدد مدنظر {} بود'.format(computer_guess))
                # guess_button.config(state='disabled')  # Disable the button after all attempts are used
                reset_game()

            guess_entry.delete(0, 'end')  # Clear the text entry
        else:
            messagebox.showwarning('خطا', '!!!'+'حدس شما خرح از محدوده 1 تا 100 است')
    except ValueError:
        messagebox.showwarning('خطا','حدس شما نباید به صورت اعشاری یا به حروف باشد')


def reset_game():
    global computer_guess, attempt_count
    attempt_count = 0
    computer_guess = random.randint(LOWER, UPPER)
    guess_entry.delete(0, tk.END)
    status_label.config(text="شما ۵ بار شانس دارید")

# Business Theme Colors
BG_COLOR = "#2E3B55"
TEXT_COLOR = "#FFFFFF"
BTN_BG_COLOR = "#4664A2"
ENTRY_BG_COLOR = "#FFFFFF"

window = tk.Tk()
window.configure(bg=BG_COLOR)
window.geometry('300x200')
window.title('بازی حدس زدن عدد')

# Description Label
description_label = tk.Label(window, text=":" + "لطفا یک عدد بین ۱ تا ۱۰۰ حدس بزنید", bg=BG_COLOR, fg=TEXT_COLOR)
description_label.pack()

# Status Label
status_label = tk.Label(window, text='شما 5 بار شانس دارید', bg=BG_COLOR, fg=TEXT_COLOR)
status_label.pack()

# Entry Widget to take user input
guess_entry = tk.Entry(window, bg=ENTRY_BG_COLOR, fg=BG_COLOR, borderwidth=2, justify='right')
guess_entry.pack()

# Button to submit the guess
guess_button = tk.Button(window, text='حدس بزن', command=guess_number, bg=BTN_BG_COLOR, fg=TEXT_COLOR, borderwidth=0)
guess_button.pack()

exit_button = tk.Button(window, text="خروج", command=window.destroy, bg=BTN_BG_COLOR, fg=TEXT_COLOR, borderwidth=0)
exit_button.pack()

# Main loop
window.mainloop()