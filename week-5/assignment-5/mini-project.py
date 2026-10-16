numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]
choice = ""
while choice == "":
    print(
"\n=== Number Cruncher ===" \
"\n1. Find minimum"
"\n2. Find maximum"
"\n3. Search for a number"
"\n4. Sort the list"
"\n5. Quit")
    choice = input("Choose an option (1-5): ")
    print("=======================" \
    "\n")
    while choice not in ["1","2","3","4","5"]:
        choice = input("Not a valid selection. Please choose option 1-5: ")
        print("=======================" \
    "\n")
    if choice == "1": 
        min = float('inf')
        for num in numbers:
            if num < min:
                min = num
        choice=""
        print(f"Minimum value: {min}")   
    elif choice == "2":
        max = 0
        for num in numbers:
            if num > max:
                max = num
        choice=""
        print(f"Maximum value: {max}")
    elif choice == "3":
        search = 0
        match=False
        while True:
            try:
                search = int(input("Select a number to search: "))
                break
            except ValueError:
                print("Not a number. Try again.")
                print("======================="
                      "\n")
        for i in range(len(numbers)):
            if numbers[i] == search:
                match = True
                break
        if match == True:
            print(f"Found it! Present at index {i}.")
        else:
            print("That number was not found in this list.")
        choice = ""
    elif choice == "4":
        def bubble_sort(data):
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(data)-1):
                    if data[i] > data[i+1]:
                        data[i], data[i+1] = data[i+1], data[i]
                        swapped=True
            return data
        sorted = bubble_sort(numbers)
        print(f"Sorted list: {sorted}")            
        choice = ""
    elif choice == "5":
        print("Goodbye!"
              "\n")
        break
    else:
        choice = ""