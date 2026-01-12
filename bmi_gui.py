import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt # Requires: pip install matplotlib

# --- DATA STORAGE ---
def save_data(name, bmi, category):
    file_exists = os.path.isfile('bmi_data.csv')
    with open('bmi_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'BMI', 'Category'])
        writer.writerow([name, f"{bmi:.2f}", category])

# --- VISUALIZATION (Advanced Requirement) ---
def show_trends():
    bmis = []
    try:
        with open('bmi_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                bmis.append(float(row['BMI']))
        
        plt.figure(figsize=(6, 4))
        plt.plot(bmis, marker='o', color='green')
        plt.title('Your BMI Trend Over Time')
        plt.ylabel('BMI Value')
        plt.grid(True)
        plt.show() # This visualizes the result [cite: 60, 68]
    except FileNotFoundError:
        messagebox.showwarning("No Data", "Please save some results first!")

# --- LOGIC ---
def calculate_bmi():
    try:
        name = entry_name.get()
        w = float(entry_weight.get())
        h = float(entry_height.get())
        
        if h > 3: # Simple check to catch cm vs meters errors
            messagebox.showwarning("Height Error", "Please enter height in meters (e.g., 1.75)")
            return

        bmi = w / (h ** 2)
        if bmi < 18.5: cat = "Underweight"
        elif 18.5 <= bmi < 24.9: cat = "Normal weight"
        elif 25 <= bmi < 29.9: cat = "Overweight"
        else: cat = "Obese"
            
        save_data(name, bmi, cat)
        messagebox.showinfo("Result", f"BMI: {bmi:.2f}\nCategory: {cat}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# --- GUI DESIGN (Advanced Requirement) ---
root = tk.Tk()
root.title("Advanced BMI Analysis")
root.geometry("400x500")

# Bold Headings for your GUI [cite: 66]
tk.Label(root, text="User Name:", font=("Arial", 10, "bold")).pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root, text="Weight (kg):", font=("Arial", 10, "bold")).pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (meters):", font=("Arial", 10, "bold")).pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

tk.Button(root, text="Calculate & Save", command=calculate_bmi, bg="green", fg="white").pack(pady=20)
tk.Button(root, text="View BMI Trend Graph", command=show_trends, bg="blue", fg="white").pack()

root.mainloop()
