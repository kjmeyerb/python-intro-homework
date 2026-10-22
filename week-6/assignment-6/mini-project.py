numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def find_min(numbers):
    min = float('inf')
    for num in numbers:
         if num < min:
            min = num
    return min 

def find_max(numbers):
    max = 0
    for num in numbers:
        if num > max:
            max = num
    return max

def search(numbers, target):
    for i in range(len(numbers)):
        index = -1
        if numbers[i] == target:
            index = i
            break
    return index

def bubble_sort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped=True
    new_list = numbers
    return new_list

def show_menu():
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
    return choice
    
def main():
    while True:
        choice = show_menu()
        if choice == "1": 
            print("Min: ",find_min(numbers))
        elif choice == "2":
            print("Max: ",find_max(numbers))
        elif choice == "3":
            while True:
                try:
                    target = int(input("Select a number to search: "))
                    break
                except ValueError:
                    print("Not a number. Try again.")
                    print("======================="
                    "\n")
            if search(numbers, target) == -1:
               print("Not found!")
            else:
                print("Found at index",{search(numbers,target)}) 
        elif choice == "4":
            print("Sorted list: ",bubble_sort(numbers))
        else:
            print("Goodbye!")
            break           

main()