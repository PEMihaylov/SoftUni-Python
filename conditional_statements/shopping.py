budget = float(input())
video_cards = int(input())
processors_count = int(input())
ram_count = int(input())

video_cards_sum = video_cards * 250
processor_sum = (video_cards_sum * 0.35) * processors_count
ram_sum = (video_cards_sum * 0.10) * ram_count

total_sum = video_cards_sum + processor_sum + ram_sum

if video_cards > processors_count:
    total_sum = total_sum * 0.85

diff = abs(total_sum - budget)
if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")