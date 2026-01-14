BMI Calculator 
** Health Analytics System **
## **Project Overview**

Developed during my **Python Programming Internship at Oasis Infobyte**, this is a professional-grade Health Analytics Dashboard. It moves beyond a simple calculator to provide a secure, data-driven environment for tracking Body Mass Index (BMI) trends over time.

## **🛡️ Advanced Security Features**

To ensure the highest standards of software stability and data integrity, I implemented several **OWASP-aligned security practices**:

* **Input Sanitization:** Uses Regular Expressions (Regex) to filter the "User Name" field, preventing the entry of malicious characters or scripts.
* **Rate Limiting:** A built-in 2-second cooldown on the 'Calculate' button prevents brute-force data entry and ensures system stability.
* **Arithmetic Hardening:** Implements strict validation to catch `ZeroDivisionError` and negative inputs, prompting users with helpful alerts instead of allowing the app to crash.
* **Secure File Handling:** The system dynamically locates the **'bmi calculator'** directory using absolute pathing to ensure the database (`bmi_data.csv`) is always stored and accessed securely within the project folder.

## **✨ Modern UI/UX Design**

* **Cyber-Blue Aesthetic:** A high-contrast "Midnight Slate" theme with Neon Cyan accents for a modern, professional look.
* **Glassmorphism:** A semi-transparent input card that provides a sleek, layered visual effect.
* **Dynamic Visuals:** Includes a **Circular Status Ring** that updates in real-time to visualize the health category alongside the numerical result.
* **Interactive Feedback:** Custom hover effects on "Pill-shaped" buttons and focused entry fields for an intuitive user experience.

## **📊 Data Analysis**

* **Persistent Storage:** All health metrics are logged to a single, unified CSV file.
* **Trend Visualization:** Integrated with **Matplotlib** to generate dark-themed line graphs, allowing users to analyze their BMI progress over time.

## **🛠️ Technical Stack**

* **Language:** Python 3.10+
* **GUI:** Tkinter
* **Visualization:** Matplotlib
* **Data:** CSV & OS Pathing
* **Security:** Re (Regex) & Time libraries

## **How to Run**

1. **Clone the Repo:** `git clone https://github.com/[YourUsername]/OIBSIP.git`
2. **Install Requirements:** `pip install matplotlib`
3. **Launch:** Navigate to the `bmi calculator` folder and run `python bmi_gui.py`.

---

**#oasisinfobyte #python #programming #cybersecurity #datavisualization #internship**
