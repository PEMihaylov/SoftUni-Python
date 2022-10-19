sentence = []
args = input().split(', ')
word = [i for i in args]
sentence.append(word)

kwargs = dict(UNI="Uni", Grate="Great")

for key, value in kwargs.items():
    if key in sentence:
        sentence = list(map(lambda x: x.replace(key, kwargs[key])))

print(sentence)