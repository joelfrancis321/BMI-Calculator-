BMI Calculator 

## Project Overview

This project came out of a Python Programming Internship at Oasis Infobyte. It’s a GUI app that lets users compute their Body Mass Index (BMI) and follow their health journey with clear data visuals.

## Key Features

- User-Friendly GUI: A clean, modern windowed interface built with Tkinter.

- Automated Data Storage: Every calculation gets saved to a CSV so you can look back at past results.

- Trend Visualization: A “View Trends” option uses Matplotlib to show BMI history as a line graph.

- Smart Input Validation: Gentle error handling if something non-numeric or out of range is entered.

## How It Works

1. Input: Users enter their Name, Weight (kg), and Height (m).

2. Logic: The program uses the BMI formula.

3. Classification: BMI falls into Underweight, Normal, Overweight, or Obese according to standard ranges.

4. Storage & Graphics: Data is saved to bmi_data.csv, which the app reads to build the trend graph.

## Installation & Usage

1. Install Dependencies:
```bash
pip install matplotlib
```

2. Run the Application:
```bash
python bmi_gui.py
```

#oasisinfobyte #internship #python #programming #datavisualization


