data = input()
company_book = {}
while data != "End":
    company_name, employee_id = data.split(" -> ")
    if company_name not in company_book:
        company_book[company_name] = []

    if employee_id not in company_book[company_name]:
        company_book[company_name].append(employee_id)
    elif employee_id in company_book[company_name]:
        company_book[company_name].append(employee_id)
        company_book[company_name] = company_book[company_name][:-1]

    data = input()

for company in company_book.keys():
    print(company)
    for user in company_book[company]:
        print(f"-- {user}")
