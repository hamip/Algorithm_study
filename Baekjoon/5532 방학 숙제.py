l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a % c != 0:
    math = a // c + 1
else:
    math = a // c

if b % d != 0:
    lang = b // d + 1
else:
    lang = b // d

print(l - max(math, lang))
