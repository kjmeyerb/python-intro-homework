while True:
    value = input("Enter a positive integer: ")
    try:
        num = float(value)
    except ValueError:
        print("Yikes, that's not a number. Try again.")
        continue
    if int(value) <= 0:
        print("Oops, that's not positive! Try again. ")
    else:
        print(f"Great job! {value} is positive.")
        break

    



