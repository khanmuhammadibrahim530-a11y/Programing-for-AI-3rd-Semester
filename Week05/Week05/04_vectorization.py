import numpy as np

temperatures = np.array([20, 25, 30, 35, 40]) 
fahrenheit = temperatures * 9 / 5 + 32 
marks = np.array([55, 67, 72, 88, 91]) 
adjusted = np.minimum(marks + 5, 100) 
normalized = (marks - marks.min()) / (marks.max() - marks.min())

print(np.round(normalized, 2))

age = np.array([20,40,60])
income = np.array([30000,150000,3000000])

normalized_age = (age - age.min()) / (age.max() - age.min())
normalized_income = (income - income.min()) / (income.max() - income.min())
print(np.round(normalized_age, 2))
print(np.round(normalized_income, 2))
scores = np.array([[70, 75, 80], [60, 65, 70], [85, 90, 95]])
bonus = np.array([2, 3, 5])
adjusted_scores = scores + bonus
