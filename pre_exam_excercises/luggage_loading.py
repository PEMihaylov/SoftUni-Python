trunk_volume = float(input())
suitcase_count = 0
loaded_suitcases = 0
suitcase_volume = input()
operated_volume = trunk_volume

while suitcase_volume != "End":
    current_suitcase = float(suitcase_volume)
    suitcase_count += 1

    if operated_volume < current_suitcase:
        break

    if suitcase_count % 3 == 0:
        current_suitcase = current_suitcase * 1.1

    operated_volume -= current_suitcase
    loaded_suitcases += 1

    suitcase_volume = input()

if suitcase_volume == "End":
    print("Congratulations! All suitcases are loaded!")
else:
    print("No more space!")

print(f"Statistic: {loaded_suitcases} suitcases loaded.")