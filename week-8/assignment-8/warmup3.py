file= "../data/missing.txt"
try:
    with open(file, "r"):
        pass
except FileNotFoundError:
    print(f"{file} was not found.")