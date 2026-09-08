usd = float(input("Enter amount in USD: "))
exchange_rate = float(input("Enter exchange rate: "))

local_amount = usd * exchange_rate

print("Converted amount:", round(local_amount, 2))