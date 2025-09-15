def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    Applies discount only if it's 20% or higher.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return round(final_price, 2)
    else:
        return round(price, 2)

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied! Final price: ${final_price}")
    else:
        print(f"No discount applied. Final price remains: ${final_price}")
except ValueError:
    print("Please enter valid numeric values for price and discount.")