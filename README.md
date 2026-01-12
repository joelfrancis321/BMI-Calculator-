BMI Calculator 

## Project Overview
This one came together during a Python Programming Internship at Oasis Infobyte. It’s a polished GUI app that lets you compute BMI, keep a health history, and spot trends over time. Security-conscious and built with solid practices.

What it does best

- Secure, clean GUI: A simple, distraction-free interface crafted with Tkinter on a plain white backdrop for easy focus.
- Input protection: Uses regular expressions to keep the name field clean and safe from weird input.
- Gentle pacing: A cooldown between calculations to avoid spamming and keep things stable.
- Data keeping: Automatically saves Name, BMI, and Category to a persistent CSV file.
- Visual trends: A “View Trends” button opens a Matplotlib line graph of BMI history.

 ### **How it Works**

> * **Accurate Logic:** Implements the standard BMI formula where weight is divided by height squared.
> * **Smart Validation:** Includes logic to catch common user errors, such as entering height in centimeters instead of meters.
> * **Secure Input:** Employs **Input Sanitization** to filter out special characters in the name field, protecting the application from unintended behavior.
> * **Rate Limiting:** Features a built-in cooldown to prevent excessive calculations in a short period, ensuring a stable user experience.



### **1. Technical Stack**

Language: Python 3.x 

GUI Library: Tkinter (for the graphical interface) 
 
Data Visualization: Matplotlib (for trend analysis and graphs)
  
Data Storage: CSV (Comma Separated Values) for persistent historical records 

Security: Regular Expressions (Regex) for input sanitization and `time` module for rate limiting



How to run

1. Download "bmi_gui.py"
2) Open a terminal or your code editor (VS Code works fine)  
3) Run: python bmi_gui.py

#oasisinfobyte #internship #python #programming #cybersecurity #datavisualization
