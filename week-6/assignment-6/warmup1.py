def greet(name, greeting="Hello"):
    print(f"{greeting}, {name.capitalize()}!")

if __name__ == "__main__":
    greet("Paz")
    greet("Paz", "Hola")
    greet("Paz", greeting="Hey")