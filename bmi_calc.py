def run_bmi_calculator():
    print("bmi calculator")
    
    while True:
        try:
            # Step 1: Input Validation 
            weight = float(input("\nEnter weight in kg (or '0' to exit): "))
            if weight == 0:
                print("Closing the program...")
                break
                
            height = float(input("Enter height in meters (e.g., 1.75): "))

            if weight < 0 or height <= 0:
                print("Error: Please enter positive values for weight and height.")
                continue

            # Step 2: BMI Calculation 
            # Formula: weight / (height * height)
            bmi = weight / (height ** 2)

            # Step 3: Categorization [cite: 65]
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"

            # Step 4: Display Result [cite: 58]
            print(f"\nYour BMI is: {bmi:.2f}")
            print(f"Health Category: {category}")
            print("-" * 40)

        except ValueError:
            print("Invalid input! Please enter numeric values only.")

if __name__ == "__main__":
    run_bmi_calculator()