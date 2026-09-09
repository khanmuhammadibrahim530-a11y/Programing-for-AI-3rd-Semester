values = []

for number in range(1, 6):
    values.append(number ** 2)

values_comp = [number ** 2 for number in range(1, 6)]

print(values)
print(values_comp)
even_numbers = [number for number in range(1, 51) if number % 2 == 0]

odd_numbers = [number for number in range(1, 51) if number % 2 != 0]

print("Even:", even_numbers)
print("Odd:", odd_numbers)