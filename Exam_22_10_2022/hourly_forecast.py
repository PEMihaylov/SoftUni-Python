def forecast(*args):
    weather = {"Sunny": [], "Cloudy": [],  "Rainy": []}

    for item in args:
        if item[1] not in weather.keys():
            weather[item[1]] = []
        weather[item[1]].append(item[0])

    weather = dict(sorted(weather.items(), key=lambda x: x[0]))

    result = []

    for key, value in weather.items():
        for loc in sorted(value):
            result.append(f"{loc} - {key}")
    sunny_result = ""
    cloudy_result = ""
    rainy_result = ""
    for word in result:
        if "Sunny" in word:
            sunny_result += word + "\n"
        elif "Cloudy" in word:
            cloudy_result += word + "\n"
        elif "Rainy" in word:
            rainy_result += word + "\n"

    final_result = sunny_result + cloudy_result + rainy_result


    return final_result

#
#
# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))
# #

# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
