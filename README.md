BMI Calculator 
** Health Analytics System **

## **Project Overview**

This project was developed for the **Oasis Infobyte Python Programming Internship**. It is an advanced, dark-themed **Health Analytics Dashboard** that calculates Body Mass Index (BMI) and provides longitudinal health tracking through data visualization.

## **🚀 Key Features**

* Modern Cyber-Blue GUI:** A high-end interface featuring a **Glassmorphism** card design, neon blue accents, and a pitch-black background for maximum visual impact.
* Dynamic Result Gauge:** Includes a custom **Status Ring** that visually displays the BMI result, providing instant feedback alongside numerical data.
* Trend Visualization:** Integrated with **Matplotlib** to generate dark-themed line graphs of the user's health history.
* Persistent Data Storage:** Automatically logs and manages user data in a `bmi_data.csv` file for historical analysis.

## **🛡️ Security & Performance**

Following **OWASP best practices**, this application includes:

* Rate Limiting:** A 2-second cooldown prevents button spamming and ensures application stability.
* Input Sanitization:** Uses **Regex (Regular Expressions)** to filter the name field, ensuring only valid text is accepted and preventing code injection.
* Strict Type Checking:** Validates all numeric inputs to prevent "Centimeter vs. Meter" errors and non-numeric crashes.

## **🛠️ Technical Stack**

* Language:** Python 3.10+
* GUI Framework:** Tkinter
* Visualization:** Matplotlib
* Data Handling:** CSV & OS libraries
* Security:** Re (Regex) & Time libraries

## **How to Run**

1. Clone this repository**: `git clone [Your Repo Link]`
2. Install dependencies**: `pip install matplotlib`
3. Launch the System**: `python bmi_gui.py`

#oasisinfobyte #internship #python #programming #cybersecurity #datavisualization
