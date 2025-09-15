def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount.
    
    Parameters:
    - price (float): Original price of the item.
    - discount_percent (float): Discount percentage to apply.
    
    Returns:
    - float: Final price after discount if discount is 20% or higher,
             otherwise returns the original price.
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return round(final_price, 2)
    else:
        return round(price, 2)