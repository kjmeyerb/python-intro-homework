#Warmup 2: Functions that Return Values
#Write two functions:

#celsius_to_fahrenheit(c) — converts Celsius to Fahrenheit using (c * 9/5) + 32
#fahrenheit_to_celsius(f) — converts Fahrenheit to Celsius using (f - 32) * 5/9
#Call each with a few test values and print the results. Use f-strings and round to one decimal place.

def celcius_to_fahrenheit(c):
    to_scale="fahrenheit"
    converted=(c * 9/5) + 32
    return to_scale, converted

def fahrenheit_to_celsius(f):
    to_scale="celcius"
    converted=(f - 32) * 5/9
    return to_scale, converted

def print_conversion(temp, initial_scale):
    if initial_scale=="fahrenheit":
        to_scale, converted=fahrenheit_to_celsius(temp)
    if initial_scale=="celcius":
        to_scale, converted=celcius_to_fahrenheit(temp)
    print(f"{temp}° {initial_scale.capitalize()} is {converted:.1f}° {to_scale.capitalize()}")

print_conversion(0, "celcius")
print_conversion(100, "celcius")
print_conversion(-212, "celcius")
print_conversion(35, "celcius")
print_conversion(32, "fahrenheit")
print_conversion(212, "fahrenheit")
print_conversion(0, "fahrenheit")
print_conversion(43, "fahrenheit")