import tkinter as tk
from tkinter import messagebox
import csv
import os
import sys
import time
import re
import matplotlib.pyplot as plt
import math

# --- CONFIGURATION & ASSETS ---
# Ensure we are working in the script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(script_dir, 'bmi_data.csv')
print(f"Final Database Path: {DATA_FILE}")

THEME = {
    "bg": "#0b0d0f",          # Pitch Black
    "card_bg": "#14171a",     # Dark Charcoal (Glass-like)
    "primary": "#00ecff",     # Neon Cyan
    "primary_hover": "#00c4d6",
    "text_main": "#ffffff",
    "text_muted": "#8899a6",
    "danger": "#ff4b2b",
    "font_main": "Verdana",
}

# --- CUSTOM UI CLASSES ---

class RoundedButton(tk.Canvas):
    def __init__(self, parent, text, command, width=200, height=50, radius=25, 
                 bg_color=THEME["primary"], fg_color="#000000", hover_color=THEME["primary_hover"],
                 is_outline=False):
        super().__init__(parent, width=width, height=height, bg=THEME["card_bg"], highlightthickness=0)
        self.command = command
        self.text = text
        self.radius = radius
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.hover_color = hover_color
        self.is_outline = is_outline
        self.width = width
        self.height = height
        
        self.draw(self.bg_color)
        
        self.bind("<Enter>", lambda e: self.draw(self.hover_color))
        self.bind("<Leave>", lambda e: self.draw(self.bg_color))
        self.bind("<Button-1>", lambda e: self.on_click())

    def draw(self, color):
        self.delete("all")
        r = self.radius
        w, h = self.width, self.height
        
        if self.is_outline:
            # Draw outline only
            self.create_oval(1, 1, 2*r, 2*r, outline=color, width=2)
            self.create_oval(w-2*r, 1, w-1, 2*r, outline=color, width=2)
            self.create_oval(1, h-2*r, 2*r, h-1, outline=color, width=2)
            self.create_oval(w-2*r, h-2*r, w-1, h-1, outline=color, width=2)
            
            self.create_line(r, 1, w-r, 1, fill=color, width=2)
            self.create_line(1, r, 1, h-r, fill=color, width=2)
            self.create_line(w-1, r, w-1, h-r, fill=color, width=2)
            self.create_line(r, h-1, w-r, h-1, fill=color, width=2)
            
            fill_color = color # Text color becomes the accent color
        else:
            # Filled pill
            self.create_oval(0, 0, 2*r, 2*r, fill=color, outline=color)
            self.create_oval(w-2*r, 0, w, 2*r, fill=color, outline=color)
            self.create_oval(0, h-2*r, 2*r, h, fill=color, outline=color)
            self.create_oval(w-2*r, h-2*r, w, h, fill=color, outline=color)
            
            self.create_rectangle(r, 0, w-r, h, fill=color, outline=color)
            self.create_rectangle(0, r, w, h-r, fill=color, outline=color)
            fill_color = self.fg_color

        self.create_text(w/2, h/2, text=self.text, fill=fill_color, 
                         font=(THEME["font_main"], 10, "bold"))

    def on_click(self):
        # Flash effect
        self.draw("#ffffff") 
        self.update()
        time.sleep(0.05)
        self.draw(self.bg_color)
        self.command()

class StatusRing(tk.Canvas):
    def __init__(self, parent, width=160, height=160, thickness=12):
        super().__init__(parent, width=width, height=height, bg=THEME["bg"], highlightthickness=0)
        self.thickness = thickness
        self.width = width
        self.height = height
        self.draw_base()
        
    def draw_base(self):
        self.delete("all")
        m = 10 # margin
        w = self.width - 2*m
        # Background track
        self.create_oval(m, m, m+w, m+w, outline="#2c3e50", width=self.thickness)
        
        # Center Text
        self.val_text = self.create_text(self.width/2, self.height/2 - 12, text="BMI SCORE", 
                                        fill=THEME["text_muted"], font=(THEME["font_main"], 8))
        self.res_text = self.create_text(self.width/2, self.height/2 + 8, text="--.--", 
                                        fill="#fff", font=(THEME["font_main"], 20, "bold"))

    def update_val(self, bmi_value, color):
        self.delete("highlight")
        m = 10
        w = self.width - 2*m
        
        # Calculate angle (Max BMI 50 for full circle approx, keeping 270 degree arc mostly for aesthetics)
        # Let's do a full 360 map where 50 BMI = 360 deg
        angle = min((bmi_value / 50) * 359.9, 359.9)
        
        # Draw dynamic arc
        # Tkinter arc start is 3 o'clock (0), goes counter-clockwise.
        # Let's start from top (90)
        self.create_arc(m, m, m+w, m+w, start=90, extent=-angle, 
                        style="arc", outline=color, width=self.thickness, tags="highlight")
        
        self.itemconfig(self.res_text, text=f"{bmi_value:.2f}", fill=color)

# --- APP LOGIC ---

last_execution_time = 0
COOLDOWN_SECONDS = 2

def save_data(name, bmi, category):
    try:
        file_exists = os.path.isfile(DATA_FILE)
        with open(DATA_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'BMI', 'Category'])
            writer.writerow([name, f"{bmi:.2f}", category])
    except PermissionError:
        messagebox.showerror("Database Error", "Please close the CSV file if it is open in another program")

def show_trends():
    bmis = []
    try:
        with open(DATA_FILE, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                bmis.append(float(row['BMI']))
        
        # Dark Theme Graph matched to dashboard
        plt.style.use('dark_background')
        fig, ax = plt.subplots(figsize=(8, 5))
        fig.patch.set_facecolor(THEME["bg"])
        ax.set_facecolor(THEME["bg"])
        
        ax.plot(bmis, marker='o', color=THEME["primary"], linewidth=2.5, markersize=8, 
                markerfacecolor=THEME["bg"], markeredgewidth=2)
        
        ax.set_title('BMI TREND HISTORY', fontsize=14, color=THEME["primary"], fontname=THEME["font_main"], pad=20, fontweight='bold')
        ax.set_ylabel('BMI SCORE', color=THEME["text_muted"], fontsize=10)
        
        # Grid Customization
        ax.grid(True, linestyle='--', color=THEME["primary"], alpha=0.15)
        ax.spines['bottom'].set_color(THEME["text_muted"])
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_color(THEME["text_muted"])
        
        ax.tick_params(axis='x', colors=THEME["text_muted"])
        ax.tick_params(axis='y', colors=THEME["text_muted"])
        
        plt.tight_layout()
        plt.show()
    except FileNotFoundError:
        messagebox.showwarning("System Alert", "No metrics found in database.")

def calculate_bmi():
    global last_execution_time
    current_time = time.time()
    
    if current_time - last_execution_time < COOLDOWN_SECONDS:
        return
    
    try:
        name = entry_name.get().strip()
        if not re.match("^[a-zA-Z ]*$", name) or not name:
            messagebox.showerror("Input Error", "Please enter a valid full name.")
            return

        w_val = entry_weight.get()
        h_val = entry_height.get()
        
        if not w_val or not h_val:
            raise ValueError

        w = float(w_val)
        h = float(h_val)
        
        if w <= 0 or h <= 0:
            messagebox.showwarning("Arithmetic Error", "Values must be greater than zero")
            return
        
        if h > 3:
            messagebox.showwarning("Logic Error", "Height is in meters (should be < 3.0).")
            return

        bmi = w / (h ** 2)
        last_execution_time = current_time 
        
        # Categorization
        if bmi < 18.5: 
            cat, color = "UNDERWEIGHT", "#3498db" # Blue
        elif 18.5 <= bmi < 24.9: 
            cat, color = "NORMAL WEIGHT", "#2ecc71" # Green
        elif 25 <= bmi < 29.9: 
            cat, color = "OVERWEIGHT", "#f1c40f" # Yellow
        else: 
            cat, color = "OBESE", THEME["danger"] # Red
            
        save_data(name, bmi, cat)
        
        # Update Visuals
        status_ring.update_val(bmi, color)
        
        lbl_cat.config(text=cat, fg=color)
        lbl_msg.config(text=f"Analysis complete for {name}")
        
    except ValueError:
        messagebox.showerror("Input Format Error", "Please enter numeric values only (e.g., 70, 1.75)")

# --- MAIN WINDOW SETUP ---
root = tk.Tk()
root.title("Health Analytics System")
root.geometry("420x780")
root.configure(bg=THEME["bg"])

# HEADER
header_frame = tk.Frame(root, bg=THEME["bg"], pady=40)
header_frame.pack(fill='x')

tk.Label(header_frame, text="HEALTH ANALYTICS SYSTEM", bg=THEME["bg"], fg=THEME["primary"], 
         font=(THEME["font_main"], 16, "bold")).pack()

# CARD CONTAINER (Glassmorphism Simulation)
# Dark semi-transparent bg with primary border
card_frame = tk.Frame(root, bg=THEME["card_bg"], highlightbackground=THEME["primary"], 
                      highlightthickness=1, padx=25, pady=35)
card_frame.pack(padx=30, fill='x')

# INPUT HELPERS
def create_styled_input(parent, label_text):
    lbl = tk.Label(parent, text=label_text, bg=THEME["card_bg"], fg=THEME["text_muted"], 
                   font=(THEME["font_main"], 9))
    lbl.pack(anchor='w', pady=(12, 5))
    
    # Using a frame to create the "glow" border effect potential, but simpler is a colored Entry bg/fg
    entry = tk.Entry(parent, bg="#0f1113", fg="white", insertbackground=THEME["primary"],
                     font=(THEME["font_main"], 11), relief="flat", bd=10)
    entry.pack(fill='x')
    
    # Active Glow line (Neon Underline)
    tk.Frame(parent, bg=THEME["primary"], height=2).pack(fill='x')
    return entry

entry_name = create_styled_input(card_frame, "FULL NAME")
entry_weight = create_styled_input(card_frame, "WEIGHT (KG)")
entry_height = create_styled_input(card_frame, "HEIGHT (METERS)")

# BUTTONS SECTION
btn_frame = tk.Frame(card_frame, bg=THEME["card_bg"], pady=25)
btn_frame.pack(fill='x')

# Primary Button (Filled)
btn_calc = RoundedButton(btn_frame, "CALCULATE & SAVE", calculate_bmi, width=280, height=45,
                         bg_color=THEME["primary"], fg_color="#000000", hover_color=THEME["primary_hover"])
btn_calc.pack(pady=8)

# Secondary Button (Outline)
btn_trend = RoundedButton(btn_frame, "VIEW TREND GRAPH", show_trends, width=280, height=40, 
                          bg_color=THEME["primary"], hover_color=THEME["primary_hover"], is_outline=True)
btn_trend.pack(pady=8)


# VISUALIZATION / RESULTS
res_frame = tk.Frame(root, bg=THEME["bg"], pady=20)
res_frame.pack(fill='both', expand=True)

status_ring = StatusRing(res_frame)
status_ring.pack()

lbl_cat = tk.Label(res_frame, text="READY", bg=THEME["bg"], fg=THEME["text_muted"], 
                   font=(THEME["font_main"], 12, "bold"))
lbl_cat.pack(pady=5)

lbl_msg = tk.Label(res_frame, text="Enter health metrics to begin", bg=THEME["bg"], fg="#444", 
                   font=(THEME["font_main"], 8))
lbl_msg.pack()

root.mainloop()