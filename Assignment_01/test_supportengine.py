from support_engine import classify_support, format_message

# --- Boundary and normal cases for classify_support() ---

# Below attendance boundary -> High priority
assert classify_support(59.9, 90, 0) == "High priority"

# High missed-submission boundary -> High priority
assert classify_support(60, 90, 4) == "High priority"

# Below attendance boundary (moderate range) -> Moderate priority
assert classify_support(74.9, 90, 0) == "Moderate priority"

# Below assignment average boundary -> Moderate priority
assert classify_support(75, 59.9, 0) == "Moderate priority"

# Moderate missed-submission boundary -> Moderate priority
assert classify_support(90, 90, 2) == "Moderate priority"

# Minimum values that still qualify as routine -> Routine monitoring
assert classify_support(75, 60, 1) == "Routine monitoring"

# Maximum valid values -> Routine monitoring
assert classify_support(100, 100, 0) == "Routine monitoring"

# --- Cases for format_message() ---

assert format_message("High priority") == "Immediate academic support is recommended."
assert (
    format_message("Moderate priority")
    == "Monitor progress and provide targeted guidance."
)
assert format_message("Routine monitoring") == "Continue routine monitoring."

print("All tests passed.")
