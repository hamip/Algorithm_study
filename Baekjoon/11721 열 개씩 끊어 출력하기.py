sentence = input()
while len(sentence) != 0:
    i = 0
    print(sentence[i:i+10])
    sentence = sentence[i+10:]
