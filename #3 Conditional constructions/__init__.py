hour_of_exam = int(input())
min_of_exam = int(input())
hour_of_arrival = int(input())
min_of_arrival = int(input())

exam_time: int = (hour_of_exam * 60) + min_of_exam
arrival_time = (hour_of_arrival * 60) + min_of_arrival
diff = abs(exam_time - arrival_time)


if exam_time < arrival_time:
    print("Late")
    if diff >= 60:
        hh = diff // 60
        mm = diff % 60
        if mm < 10:
            print(f"{hh}:0{mm:} hours after the start")
        else:
            print(f"{hh}:{mm:} hours after the start")
    else:
        print("Late")
        print(f"{hh}:{mm:} hours after the start")
else:
    print(f"{hh}:{mm:} hours after the start")

elif exam_time == arrival_time or diff <= 30:
    print("On time")
    if diff 
elif (exam_time > arrival_time) and 0 < diff <= 30:
    print("On time")
    print(f"{mm} minutes before the start")

elif (exam_time > arrival_time) and 30 < diff <= 60:
    print("Early")
    print(f"{mm} minutes before the start")
elif exam_time > arrival_time and diff > 60:
    print("Early")
    if mm < 10:
        print(f"{hh}:0{mm:} hours after the start")
    else:
        print(f"{hh}:{mm} hours before the start")

