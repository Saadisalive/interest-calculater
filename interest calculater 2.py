from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")
root.title("Interest Calculater app")
root.configure(bg ="grey")

def interest():
    try:
        Principal = float(principal_entry.get())
        time = float(time_entry.get())
        rate = float(rate_entry.get())
        
        simple_interest = (Principal * time * rate) / 100
        
        amount =Principal * (pow((1 + rate / 100),time))#The pow() function returns the value of x to the power of y (xy). If a third parameter is present, it returns x to the power of y, modulus z.
        compound_interest = amount - Principal
        
        simple_interest_label.config(text=f"Simple Interest: {simple_interest:.2f}")
        compound_interest_label.config(text=f"Compound Interest: {compound_interest:.2f}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers for all fields.")


pricipal_label = Label(root,text="Pricipal amount")
pricipal_label.grid(row=0, column=0, padx=10, pady=5)
principal_entry = Entry(root)
principal_entry.grid(row=0, column=1, padx=10, pady=5)

time_label = Label(root, text="Time Period (years):")
time_label.grid(row=1, column=0, padx=10, pady=5)
time_entry = Entry(root)
time_entry.grid(row=1, column=1, padx=10, pady=5)

rate_label = Label(root, text="Rate of Interest (%):")
rate_label.grid(row=2, column=0, padx=10, pady=5)
rate_entry = Entry(root)
rate_entry.grid(row=2, column=1, padx=10, pady=5)

calculate_button = Button(root, text="Calculate", command=interest)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

simple_interest_label = Label(root, text="Simple Interest: ")
simple_interest_label.grid(row=4, column=0, columnspan=2, padx=10, pady=5)

compound_interest_label = Label(root, text="Compound Interest: ")
compound_interest_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()