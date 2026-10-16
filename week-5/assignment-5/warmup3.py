names = ["Aisha","Mateo","Yuki", "Kwame","Priya","Liam","Amara","Ji-hoon","Camille","Rafael","Zara","Nikolai","Thandiwe","Mei","Elias"]
index = -1
search = input("Search a name: ").capitalize()
for i in range(len(names)):
    if names[i] == search:
        index = i + 1
        break
if index != -1:
    print(f"{search.capitalize()} was #{index} on the list.")
else:
    print(f"We did not find {search.capitalize()} on this list.")