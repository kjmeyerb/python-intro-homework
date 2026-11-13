numerator=input("Enter the numerator: ")
try:
    numerator=float(numerator)
    
except ValueError:
    print("That's not a number.")
else:
    denominator=input("Enter the denominator: ")
    try:
        denominator=float(denominator)
    except ValueError:
        print("That's not a number.")
    else:
        try:
            print(f"{numerator} / {denominator} = {numerator/denominator:.2f}")
        except ZeroDivisionError:
            print("Denominator cannot be zero.")