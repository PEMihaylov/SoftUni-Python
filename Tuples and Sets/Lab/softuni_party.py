guest_num = int(input())
reservation_numbers = set()

for i in range(guest_num):
    reservation_numbers.add(input())

res_code = input()
while res_code != "END":
    if res_code in reservation_numbers:
        reservation_numbers.remove(res_code)
    res_code = input()

print(len(reservation_numbers))
print('\n'.join(sorted(reservation_numbers)))