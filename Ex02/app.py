from utils import make_array
from utils import identify
import tkinter as tk
from tkinter import messagebox


def generate_and_check():
    try:
        length = int(entry.get())
        random_result = make_array.create_random_array(length)
        result_message = identify.win_or_fail(random_result)
        # messagebox.showinfo("Result", result_message)
        result_label.config(text=result_message)  # Update the label with the result message
        entry.delete(0, 'end')  # Clear the text entry
    except ValueError:
        messagebox.showwarning('Error', 'Please enter a valid integer!')
        entry.delete(0, 'end')  # Clear the text entry


# Create main window with comic font
window = tk.Tk()
window.geometry('450x300')
Font_tuple_1 = ("Comic Sans MS", 20, "bold")
Font_tuple_2 = ("Comic Sans MS", 18)
Font_tuple_3 = ("Comic Sans MS", 12)
window.configure(bg='lightgray')
window.title("Numpy")

# Create title label
label = tk.Label(window, text="Numpy Game", fg='blue', font=Font_tuple_1, bg='lightgray')
label.pack()

# create input label
label = tk.Label(window, text="Please Enter a Number:", font=Font_tuple_2, height=2, bg='lightgray')
label.pack()

# Create entry
entry = tk.Entry(window, font=Font_tuple_3)
entry.pack()

# Create button to generate and check result
button = tk.Button(window, text="Generate & Check", command=generate_and_check, font=Font_tuple_3, bg='lightgreen')
button.pack(pady=10)

# Create label to display the result
result_label = tk.Label(window, text="", fg='purple', font=Font_tuple_3, bg='lightgray')
result_label.pack()

# Create Exit
exit_button = tk.Button(window, text="Exit", command=window.destroy, bg='tomato', fg='white', font=Font_tuple_2,
                        borderwidth=2)
exit_button.pack(pady=15)

# Run the application
window.mainloop()
