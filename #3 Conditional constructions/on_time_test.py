exam_hour = int(input())
exam_min = int(input())
arrival_hour = int(input())
arrival_min = int(input())

total_min_exam = exam_hour * 60 + exam_min
total_min_arrival = arrival_hour * 60 + arrival_min
diff_time = abs(total_min_exam - total_min_arrival)

diff_hour = diff_time // 60
diff_min = diff_time % 60

if total_min_exam < total_min_arrival:
    print("Late")
elif diff_time <= 30 and total_min_exam >= total_min_arrival:
    print("On time")
elif diff_time > 30 and total_min_exam > total_min_arrival:
    print("Early")

if total_min_exam > total_min_arrival and diff_time < 60:
    print(f"{diff_min} minutes before the start")
elif total_min_exam > total_min_arrival and diff_time >= 60:
    if diff_min < 10:
        print(f"{diff_hour}:0{diff_min} hours before the start")
    else:
        print(f"{diff_hour}:{diff_min} hours before the start")
elif total_min_exam < total_min_arrival and diff_time < 60:
    print(f"{diff_min} minutes after the start")
elif total_min_exam < total_min_arrival and diff_time >= 60:
    if diff_min < 10:
        print(f"{diff_hour}:0{diff_min} hours after the start")
    else:
        print(f"{diff_hour}:{diff_min} hours after the start")