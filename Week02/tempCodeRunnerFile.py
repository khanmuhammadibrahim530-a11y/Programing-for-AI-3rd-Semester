values =[]
for number in range(1,6):
    values.append(number**2)
    values_comp=[number**2 for number in range (1,6)]
    print(values)
    print(values_comp)