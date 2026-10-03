age = int(input("How old are you? "))
if age <= 12:
    print("You are a Child.")
elif age > 12 and age <= 17:
    print("You are a Teen.")
elif age > 17 and age <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")