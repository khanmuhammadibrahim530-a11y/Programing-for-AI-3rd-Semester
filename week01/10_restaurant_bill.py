food_price = float(input("Enter food price: "))
tax_percentage = float(input("Enter tax percentage: "))
discount_percentage = float(input("Enter discount percentage: "))
service_charge = float(input("Enter service charge: "))

tax = food_price * tax_percentage / 100
after_tax = food_price + tax

discount = after_tax * discount_percentage / 100
after_discount = after_tax - discount

final_bill = after_discount + service_charge

print("Final bill:", round(final_bill, 2))