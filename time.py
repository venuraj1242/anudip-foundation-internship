# time convert

a = int(input("enter time in seconds"))
if a >= 0:
    hour = a // 3600
    y = a % 3600
    m = y // 60
    s = y % 60
else:
    print("invalid")
print(hour, "hour", m, "minutes", s, "seconds")
