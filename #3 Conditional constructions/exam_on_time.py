exam_hour = int(input())
exam_min = int(input())
hour_of_arrival = int(input())
min_of_arrival = int(input())

exam_time_min = (exam_hour * 60) + exam_min
arrival_time_min = (hour_of_arrival * 60) + min_of_arrival

diff_time = abs(exam_time_min - arrival_time_min)

if exam_time_min < arrival_time_min:
    print("Late")
    if diff_time < 60:
        hour = diff_time // 60
        min = diff_time % 60
        print(f"{diff_time} minutes after the start")
    else:
        print(f"{hour}:{min} hours after the start"
elif exam_time_min == arrival_time_min or diff_time <= 30:
    print("On time")
    if diff_time >=1 or diff_time <= 30:
        print(f"{diff_time} minutes before the start")
else:
    print("Early")
    if diff_time < 60:
        hour = diff_time // 60
        min = diff_time % 60

    elif diff_time >= 60:
        print(f"{hour}:{min} hours before the start")
