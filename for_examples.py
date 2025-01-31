#range
for i in range(1,10,2):
    print(i)

#sum with for
s = 0
for i in range(1, 11):
    s += i
    # or s = s + i -> s = ((1+10)*10)/2

print(s)

# sum with while
i = 1
while i < 10:
    print(i)
    i += 2

s = 0
i = 1
while i <= 10:
    s += i
    i += 1 #means increase i
print(s)
