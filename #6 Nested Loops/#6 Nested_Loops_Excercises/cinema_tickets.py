entrance = input()
student_count = 0
standard_count = 0
kid_count = 0
total_tickets_count = 0
while entrance != "Finish":
    movie = str(entrance)
    capacity = int(input())
    ticket_type = input()
    movie_ticket_count = 0
    while ticket_type != "End":
        movie_ticket_count += 1
        if ticket_type == "standard":
            standard_count += 1
        elif ticket_type == "student":
            student_count += 1
        elif ticket_type == "kid":
            kid_count += 1
        total_tickets_count += 1
        if movie_ticket_count == capacity:
            break
        ticket_type = input()

    percent_full = movie_ticket_count / capacity * 100
    print(f"{movie} - {percent_full:.2f}% full.")

    entrance = input()

print(f"Total tickets: {total_tickets_count}")

student_percent = student_count / total_tickets_count * 100
print(f"{student_percent:.2f}% student tickets.")

standard_percent = standard_count / total_tickets_count * 100
print(f"{standard_percent:.2f}% standard tickets.")

kid_percent = kid_count/ total_tickets_count * 100
print(f"{kid_percent:.2f}% kids tickets.")


