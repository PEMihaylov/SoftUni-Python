import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


pattern = r"([A-z\.\-]+)\@[A-z]+(\.[a-z]+)"
domains = ['.com', '.bg', '.org', '.net']

emails = input()
result = re.match(pattern, emails)
name = result.group(1)
domain = result.group(2)

while emails != "End":

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    elif "@" not in emails:
        raise MustContainAtSymbolError("Email must contain @")

    elif domain not in domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    else:
        print("Email is valid")

    emails = input()