messages = input().split()
final_message = []

for message in messages:
    number = ""
    current_message = ""
    for character in message:
        if character.isdigit():
            number += character
        else:
            break
    message = message.replace(number, "")
    number = int(number)
    current_message += chr(number)
    if len(message) >= 2:
        message = message[-1] + message[1: -1] + message[0]
    current_message += message
    final_message.append(current_message)

print(" ".join(final_message))

print(current_message)


# message = input().split()
# deciphered_message = []
#
# for word in message:
#     characters = [char for char in word if not char.isdigit()]
#     nums = [num for num in word if num.isdigit()]
#     ascii_char = [chr(int(''.join(nums)))]
#     current_word = ascii_char + characters
#     current_word[1], current_word[-1] = current_word[-1], current_word[1]
#     deciphered_message.append(''.join(current_word))
# print(' '.join(deciphered_message))



#.....moeto.........
# text = input().split()
# deciphered_message = []
#
# for word in text:
#     digit = ""
#     curr_word = ""
#     final_word = ""
#     for letter in word:
#         if letter.isdigit():
#             digit += letter
#         else:
#             curr_word += letter
#
#     num = int(digit)
#     if len(curr_word) >= 2:
#         curr_word = curr_word[-1:] + curr_word[1:-1] + curr_word[:1]
#     final_word = chr(num) + curr_word
#     deciphered_message.append(final_word)
#
#
# print(' '.join(deciphered_message))