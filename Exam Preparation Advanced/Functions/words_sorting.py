def words_sorting(*words):
    wordict = {}
    total_sum = 0

    for word in words:
        if word not in wordict.values():
            wordict[word] = []

    for word in wordict:
        curr_sum = 0
        for w in word:
            curr_sum += ord(w)
        wordict[word] = curr_sum
        total_sum += curr_sum

    if total_sum % 2 == 0:
        wordict_sorted = sorted(wordict.items(), key=lambda x: x[0])
    elif total_sum % 2 != 0:
        wordict_sorted = sorted(wordict.items(), key=lambda x: -x[1])

    result = []
    for key, value in wordict_sorted:
        result.append(f"{key} - {value}")

    return '\n'.join(result)

#SoftUni autor solution.......................

# def words_sorting(*args):
#     words = {word: sum(map(ord, word)) for word in args}
#     result_str = []
#
#     if not sum(words.values()) % 2 == 0:
#         for word in sorted(words.items(), key=lambda x: -x[1]):
#             result_str.append(f"{word[0]} - {word[1]}")
#     else:
#         for word in sorted(words.items(), key=lambda x: x[0]):
#             result_str.append(f"{word[0]} - {word[1]}")
#
#     return "\n".join(result_str)

#....................................................
print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
