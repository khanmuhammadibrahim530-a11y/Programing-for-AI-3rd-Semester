# G1. Missing colon

# Error: Missing colon (:) after the for loop condition.
# Cause: Python requires a colon at the end of a for loop statement.
# Fix: Add a colon after range(5).

for i in range(5):
    print(i)


# G2. Assignment and comparison

# Error: Assignment operator (=) is used instead of comparison operator (==).
# Cause: = assigns a value, while == compares two values.
# Fix: Use == to compare x with 5.

x = 5

if x == 5:
    print(x)


# G3. Infinite loop

# Error: The while loop is infinite.
# Cause: The value of x never changes, so x < 10 always remains True.
# Fix: Increase x inside the loop so the condition eventually becomes False.

x = 0

while x < 10:
    print(x)
    x = x + 1