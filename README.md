BMI Calculator 

## Project Overview
This one came together during a Python Programming Internship at Oasis Infobyte. It’s a polished GUI app that lets you compute BMI, keep a health history, and spot trends over time. Security-conscious and built with solid practices.

What it does best

- Secure, clean GUI: A simple, distraction-free interface crafted with Tkinter on a plain white backdrop for easy focus.
- Input protection: Uses regular expressions to keep the name field clean and safe from weird input.
- Gentle pacing: A cooldown between calculations to avoid spamming and keep things stable.
- Data keeping: Automatically saves Name, BMI, and Category to a persistent CSV file.
- Visual trends: A “View Trends” button opens a Matplotlib line graph of BMI history.

How it works

BMI formula: BMI = weight (kg) / (height (m))  
Categories: Underweight, Normal, Overweight, or Obese, based on standard ranges.  
Helpful error handling: Includes checks for centimeters vs. meters (like catching 175 when 1.75 was intended).

Getting it up and running

Prereqs: Python plus a plotting library

pip install matplotlib

How to run

1. Download "bmi_gui.py"
2) Open a terminal or your code editor (VS Code works fine)  
3) Run: python bmi_gui.py

#oasisinfobyte #internship #python #programming #cybersecurity #datavisualization
