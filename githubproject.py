# app.py
# Running Hours Tracker
# This program estimates your weekly running time based on today's running hours.
# It includes input prompts, calculations, error handling, and clear output.

# 1. Welcome message
print("Welcome to the Running Hours Tracker!")

# 2. Ask the user for input
hours_input = input("How many hours did you run today? ")

# 3. Convert input and handle errors
try:
    hours_today = float(hours_input)
except ValueError:
    print("Please enter a valid number for hours (example: 1 or 1.5).")
    exit()

# 3 (continued). Perform calculation
weekly_hours = hours_today * 7

# 4. Display results clearly
print()
print(f"Since you ran {hours_today:.2f} hour(s) today,")
print(f"you are on pace to run about {weekly_hours:.2f} hour(s) this week!")

# 6. Program is complete
