print(not True and False) 
    # FALSE: not True is False, False is False; False and False is False.
print(True or False and False) 
    # TRUE: True is True, False and False is False, and operators are evaluated before or operators; True OR False is True.
print(not (5 > 3)) 
    # FALSE: 5 > 3 is True; not True is False.
print(10 == 10 and 4 != 4)
    # FALSE: 10 == 10 is True, 4 != 4 is False; True AND False is False.
print(not False or not True)
    # TRUE: not False is True, not True is False, no operators are evaluated first; True OR False is True.