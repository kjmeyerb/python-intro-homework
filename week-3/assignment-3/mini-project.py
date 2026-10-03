day = input("What day is it today? ").lower()
time = input("Is it morning, afternoon, or evening? ").lower()

if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("I'm sorry, '" + day + "' is not a recognized day of the week. Try again.")
elif time not in ["morning", "afternoon", "evening"]:
    print("I'm sorry, '" + time + "' is not a valid response. Try again.")
elif day == "friday" and time == "evening":
    print("Check for some nearby dance social, like salsa or swing.")
elif day == "monday" and time == "morning":
    print("Monday mornings are the worst. Go get some coffee!")
elif day == "friday" and time == "afternoon":
    print("You could attend Salat al-Jumu'ah at a nearby mosque.")
elif day == "satuday" and time == "morning":
    print("You could attend Shabbat services at a nearby synagogue.")
elif day == "sunday" and time == "morning":
    print("You could attend a service at a nearby church.")
elif day == "sunday" and time == "evening":
    print("Try to meal prep to make the week less hectic.")
elif day == "saturday" or (day == "sunday" and time == "afternoon") or (day == "friday" and time == "evening"):
    print("It's the perfect time to relax with family and friends.")
elif day in ["monday", "tuesday", "wednesday", "thursday"] and time == "evening":
    print("Spend some time resting before the grind starts again tomorrow.")
elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"] and (time == "morning" or time == "afternoon"):
    print("It's the grind! Get some work done.")
else:
    print("We have no suggestions for this time. Go get creative!")