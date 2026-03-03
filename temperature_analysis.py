# Name: [Adharsh Kumar]
# Roll Number: [2602439]
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]


highest = temperatures[0]
lowest = temperatures[0]

for temp in temperatures:
    if temp > highest:
        highest = temp
    if temp < lowest:
        lowest = temp

print("Highest Temperature:", str(highest) + "°C", "  Lowest Temperature:", str(lowest) + "°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]

hot_days = 0

for temp in temperatures:
    if temp <= 30:
        continue  # skip non-hot days
    hot_days += 1

print("Hot Days (>30°C):", hot_days)

print("\n===== Task 3: Alert System =====")
temperatures = [28, 32, 35, 40, 31, 33, 30]

hot_days_before_alert = 0
day_number = 0

for temp in temperatures:
    day_number += 1
    if temp >= 40:
        print("Hot Days before alert:", hot_days_before_alert, "  Alert! Extreme temperature", str(temp) + "°C", "detected on Day", day_number)
        break
    if temp > 30:
        hot_days_before_alert += 1
