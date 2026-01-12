import tkinter as tk
from tkinter import messagebox
import csv
import os
import time
import re
import matplotlib.pyplot as plt

# --- SECURITY & STORAGE LOGIC ---
last_execution_time = 0
COOLDOWN_SECONDS = 2 

def save_data(name, bmi, category):
    file_exists = os.path.isfile('bmi_data.csv')
    with open('bmi_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(['Name', 'BMI', 'Category'])
        writer.writerow([name, f"{bmi:.2f}", category])

def show_trends():
    bmis = []
    try:
        with open('bmi_data.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                bmis.append(float(row['BMI']))
        
        # Professional Dark Graph Theme
        plt.style.use('dark_background')
        plt.figure(figsize=(6, 4))
        plt.plot(bmis, marker='o', color='#2ecc71', linewidth=2, markersize=8)
        plt.title('Health Progress: BMI Trend Analysis', fontsize=12, color='white', fontweight='bold')
        plt.ylabel('BMI Value', color='white')
        plt.grid(True, linestyle='--', alpha=0.3)
        plt.show()
    except FileNotFoundError:
        messagebox.showwarning("No Data", "Please save some results first!")

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
            messagebox.showerror("Input Error", "Please enter a valid name.")
            return

        w = float(entry_weight.get())
        h = float(entry_height.get())
        
        if h > 3:
            messagebox.showwarning("Format Error", "Use meters (e.g., 1.75).")
            return

        bmi = w / (h ** 2)
        last_execution_time = current_time 
        
        # Color-coded results for professional UI
        if bmi < 18.5: cat, color = "UNDERWEIGHT", "#f1c40f"
        elif 18.5 <= bmi < 24.9: cat, color = "NORMAL WEIGHT", "#2ecc71"
        elif 25 <= bmi < 29.9: cat, color = "OVERWEIGHT", "#e67e22"
        else: cat, color = "OBESE", "#e74c3c"
            
        save_data(name, bmi, cat)
        label_display.config(text=f"{name}'s BMI: {bmi:.2f}", fg="white")
        label_status.config(text=cat, fg=color)
        
    except ValueError:
        messagebox.showerror("Error", "Enter numeric values for weight/height.")

# --- PROFESSIONAL DARK THEME DESIGN ---
root = tk.Tk()
root.title("Oasis Infobyte | Health Analytics")
root.geometry("420x600")
root.configure(bg='#1e272e') # Deep charcoal background

# Header Section
header = tk.Frame(root, bg='#2f3640', height=100)
header.pack(fill='x')
tk.Label(header, text="BMI CALCULATOR", bg='#2f3640', fg='#dcdde1', font=("Impact", 22)).pack(pady=25)

# Main Card Container
card = tk.Frame(root, bg='#2f3640', padx=40, pady=40, highlightthickness=0)
card.place(relx=0.5, rely=0.5, anchor='center')

# Modern Label & Entry Style
style_label = {"bg": "#2f3640", "fg": "#f5f6fa", "font": ("Segoe UI", 10, "bold")}
style_entry = {"font": ("Segoe UI", 11), "bg": "#dcdde1", "bd": 0, "relief": "flat"}

tk.Label(card, text="FULL NAME", **style_label).pack(anchor='w')
entry_name = tk.Entry(card, **style_entry)
entry_name.pack(fill='x', pady=(5, 20), ipady=5)

tk.Label(card, text="WEIGHT (KG)", **style_label).pack(anchor='w')
entry_weight = tk.Entry(card, **style_entry)
entry_weight.pack(fill='x', pady=(5, 20), ipady=5)

tk.Label(card, text="HEIGHT (METERS)", **style_label).pack(anchor='w')
entry_height = tk.Entry(card, **style_entry)
entry_height.pack(fill='x', pady=(5, 30), ipady=5)

# High-Contrast Action Buttons
btn_calc = tk.Button(card, text="CALCULATE & SAVE", command=calculate_bmi, bg='#2ecc71', fg='#1e272e', 
                     font=("Segoe UI", 11, "bold"), relief='flat', cursor='hand2', activebackground="#27ae60")
btn_calc.pack(fill='x', ipady=10)

tk.Button(card, text="VIEW HISTORY TRENDS", command=show_trends, bg='#3498db', fg='white', 
          font=("Segoe UI", 9, "bold"), relief='flat', cursor='hand2', activebackground="#2980b9").pack(fill='x', pady=(15, 0), ipady=5)

# Result Section at the Bottom
label_display = tk.Label(root, text="", bg='#1e272e', font=("Segoe UI", 12))
label_display.pack(side='bottom', pady=(0, 5))
label_status = tk.Label(root, text="", bg='#1e272e', font=("Segoe UI", 15, "bold"))
label_status.pack(side='bottom', pady=(0, 40))

root.mainloop()