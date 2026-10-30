password = input("Type a test password: ")

def check(pw):
    if len(pw) < 8:
        print("weak: too short")
    elif len(pw) < 12:
        print("medium: okay length, but use longer")
    else:
        print("strong length: good length")

def has_digit(pw):
    for ch in pw:
        if ch.isdigit():
            return True
    return False

print(f"length: {len(password)}")
check(password)
print(f"has number: {has_digit(password)}")
