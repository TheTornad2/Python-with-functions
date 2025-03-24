from datetime import datetime
import math

# Epic Introduction
print(
    """
+----------------------------------------+
|                                        |
|         TIRE VOLUME CALCULATOR         |
|                                        |
+----------------------------------------+
"""
)

# User input to start the program
print("Please enter the tire specifications in millimeters and inches.")
try:
    width = int(input("Enter tire width in mm (example: 205): "))
    aspect_ratio = int(input("Enter aspect ratio (example: 60): "))
    diameter = int(input("Enter wheel diameter in inches (example: 15): "))
except ValueError:
    print("Invalid input. Please enter whole numbers.")
    exit()

# Calculate tire volume using the formula given in the class (what a hard thing to read)
volume = (
    math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)
) / 10**10

# return the result to the user
print(f"\nThe approximate volume is {volume:.2f} liters")

# Create data record with current date
current_date = datetime.now().strftime("%Y-%m-%d")
data_line = f"{current_date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}"

# Enhanced feature: Purchase inquiry
buy_decision = input("\nWould you like to buy these tires? (yes/no): ").lower()
if buy_decision.startswith("y"):
    phone = input("Enter your phone number or Email: ").strip()
    data_line += f", {phone}"

# Save data and create a file where you run the program giving you all the Tire volumes you have calculated
# If the file doesn't exist, it will be created
with open("volumes.txt", "a") as file:
    file.write(data_line + "\n")

# Optional confirmation message
if buy_decision.startswith("y"):
    print("Thank you! We'll contact you soon.")
