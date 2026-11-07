num=""
while isinstance(num, str):
    num=input("Enter a number: ")
    try:
        num=float(num)
    except ValueError:
        print("Not a valid number. Try again.")
    else:
        print(f"You entered {num}.")
