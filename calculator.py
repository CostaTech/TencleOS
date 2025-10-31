import tkinter as tk
from tkinter import messagebox
# Create main window
root = tk.Tk()
root.title("Calculator")
# Entry widget for input
entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)
# Button click function
def click(button_text):
   if button_text == "=":
       try:
           result = eval(entry.get())
           entry.delete(0, tk.END)
           entry.insert(0, str(result))
       except:
           messagebox.showerror("Error", "Invalid Input")
   elif button_text == "C":
       entry.delete(0, tk.END)
   else:
       entry.insert(tk.END, button_text)
# Button layout
buttons = [
   ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
   ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
   ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
   ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]
for text, row, col in buttons:
   tk.Button(root, text=text, padx=20, pady=20,
             command=lambda t=text: click(t)).grid(row=row, column=col)
root.mainloop()