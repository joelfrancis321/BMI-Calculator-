import tkinter as tk
from tkinter import messagebox
import csv
import os
import time
import re
import matplotlib.pyplot as plt

# --- SECURITY: RATE LIMITING ---
last_execution_time = 0
COOLDOWN_SECONDS = 2 

# --- DATA STORAGE ---
def save_data(name, bmi, category):
    file_exists = os.path.isfile('bmi_data.csv')
    with open('bmi_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'BMI', 'Category'])
        writer.writerow([name, f"{bmi:.2f}", category])

# --- VISUALIZATION: TREND ANALYSIS ---
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
        plt.show() # Fulfills visualization requirement [cite: 60, 68]
    except FileNotFoundError:
        messagebox.showwarning("No Data", "Please save some results first!")

# --- LOGIC: SECURE CALCULATION ---
def calculate_bmi():
    global last_execution_time
    current_time = time.time()
    
    # Rate Limiting
    if current_time - last_execution_time < COOLDOWN_SECONDS:
        messagebox.showwarning("Rate Limit", "Please wait between calculations.")
        return
    
    try:
        # Input Sanitization
        name = entry_name.get().strip()
        if not re.match("^[a-zA-Z ]*$", name) or not name:
            messagebox.showerror("Input Error", "Invalid name format.")
            return

        w = float(entry_weight.get())
        h = float(entry_height.get())
        
        if h > 3: # Catching meter vs cm errors [cite: 63]
            messagebox.showwarning("Height Error", "Please enter height in meters (e.g., 1.75)")
            return

        bmi = w / (h ** 2)
        last_execution_time = current_time 
        
        if bmi < 18.5: cat = "Underweight"
        elif 18.5 <= bmi < 24.9: cat = "Normal weight"
        elif 25 <= bmi < 29.9: cat = "Overweight"
        else: cat = "Obese"
            
        save_data(name, bmi, cat) # Data storage [cite: 61, 67]
        messagebox.showinfo("Result", f"BMI: {bmi:.2f}\nCategory: {cat}")
        
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numeric values.")

# --- CLEAN GUI DESIGN ---
root = tk.Tk()
root.title("Advanced BMI Analysis")
root.geometry("400x500")
root.configure(bg='white') # Plain background

# Bold Headings [cite: 66, 70]
tk.Label(root, text="USER NAME", bg='white', font=("Arial", 10, "bold")).pack(pady=(20,5))
entry_name = tk.Entry(root, bd=1, relief="solid")
entry_name.pack()

tk.Label(root, text="WEIGHT (KG)", bg='white', font=("Arial", 10, "bold")).pack(pady=5)
entry_weight = tk.Entry(root, bd=1, relief="solid")
entry_weight.pack()

tk.Label(root, text="HEIGHT (METERS)", bg='white', font=("Arial", 10, "bold")).pack(pady=5)
entry_height = tk.Entry(root, bd=1, relief="solid")
entry_height.pack()

tk.Button(root, text="CALCULATE & SAVE", command=calculate_bmi, bg="#2c3e50", fg="white").pack(pady=20)
tk.Button(root, text="VIEW TREND GRAPH", command=show_trends, bg="#2980b9", fg="white").pack()

root.mainloop()