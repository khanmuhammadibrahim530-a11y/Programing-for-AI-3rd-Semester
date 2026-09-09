
# Part H - Traffic Signal Decision

# Read traffic density
density = input("Enter traffic density (low, medium, or high): ").lower()

# Read emergency vehicle status
emergency = input("Is an emergency vehicle present? (yes/no): ").lower()

# Decide green-light time based on traffic density
if density == "low":
    green_time = 20
elif density == "medium":
    green_time = 40
elif density == "high":
    green_time = 60
else:
    print("Invalid traffic density. Please enter low, medium, or high.")
    green_time = None

# Emergency override or normal decision
if green_time is not None:
    if emergency == "yes":
        print("Emergency override: route receives immediate green.")
    else:
        print("Normal green-light time:", green_time, "seconds")

