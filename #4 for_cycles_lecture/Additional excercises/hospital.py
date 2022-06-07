period_in_days = int(input())
doctors = 7
checked_patients = 0
unchecked_patients = 0
for days in range(1, period_in_days + 1):
    if days % 3 == 0 and unchecked_patients > checked_patients:
        doctors += 1
    patients = int(input())
    if doctors >= patients:
        checked_patients += patients
    elif doctors < patients:
        unchecked_patients += abs(doctors - patients)
        checked_patients += doctors

print(f"Treated patients: {checked_patients}.")

print(f"Untreated patients: {unchecked_patients}.")