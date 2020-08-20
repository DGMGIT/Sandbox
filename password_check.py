password = input("password:")
min_len = 3
while len(password) < min_len:
    print("too short")
    password = input("password:")
for CHARS in password:
    print("*", end="")
