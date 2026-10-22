def is_valid_score(score):
    if score >= 0 and score <= 100:
        return True
    else:
        return False

score = int(input("Enter a score: "))
if is_valid_score(score)==True:
    print("Valid score.")
else:
    print("Invalid score- must be between 0 and 100.")