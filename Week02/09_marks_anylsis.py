marks = [78, 65, 92, 85, 48, 91]

passing = []
failing = []

for mark in marks:
    if mark >= 50:
        passing.append(mark)
    else:
        failing.append(mark)

total = 0

for mark in marks:
    total += mark

average = total / len(marks)

highest = max(marks)
lowest = min(marks)

print("Passing:", passing)
print("Failing:", failing)
print("Average:", average)
print("Highest:", highest)
print("Lowest:", lowest)