day = input("What day is it today? ").lower()
time = input("Is it morning, afternoon, or evening? ").lower()

if day not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
    print("I'm sorry, '" + day + "' is not a recognized day of the week. Try again.")
if time not in ["morning", "afternoon", "evening"]:
    print("I'm sorry, '" + time + "' is not a valid response. Try again.")
elif (day == "saturday" or day == "sunday") and time == "morning":
    print("It's the weekend, go back to sleep!")
elif (day == "saturday" and (time == "afternoon" or time == "evening")) or (day == "sunday" and time == "afternoon") or (day == "friday" and time == "evening"):
    print("It's the perfect time to relax with family and friends.")
elif day in ["sunday","monday", "tuesday", "wednesday", "thursday"] and time == "evening":
    print("Spend some time resting before the grind starts again tomorrow.")
elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"] and time == "morning" or time == "afternoon":
    print("It's the grind! Get some work done.")
else:
    print("We have no suggestions for this time. Go get creative!")