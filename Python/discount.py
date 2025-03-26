"""
1. Your program asks the user for the subtotal but does not ask the user for the day of the week. Your program gets the day of the week from your computer’s operating system.

2. Your program correctly computes and prints the discount amount if applicable.

3. Your program correctly computes and prints the sales tax amount and the total amount due.

"""

from datetime import datetime


def calculate_total(subtotal):
    current_date_and_time = datetime.now()
    day_of_week = current_date_and_time.weekday()

    discount = 0
    if subtotal >= 50 and day_of_week in [1, 2]:  # Martes (1) o Miércoles (2)
        discount = subtotal * 0.10
        subtotal -= discount

    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax

    if discount > 0:
        print(f"Discount amount: ${discount:.2f}")
    print(f"Sales tax amount: ${sales_tax:.2f}")
    print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    subtotal = float(input("Please enter the subtotal: "))
    calculate_total(subtotal)

