def calculate_discount(price, discount_percent):
    
    if discount_percent >= 20:

# Calculating the discounted price
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:

# If discount is less than 20%, return original price
        return price

# Prompting the user for input of the original price and percentage discount
original_price = float(input("Enter the original price of the item: $"))
discount_percent = float(input("Enter the discount percentage: "))

# Calculating and printing the final price after applying the discount
final_price = calculate_discount(original_price, discount_percent)
print("Final price after applying the discount: $", final_price)
