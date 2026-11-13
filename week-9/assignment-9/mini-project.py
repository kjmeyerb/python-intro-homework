import os
import requests

def get_countries():
    API_KEY = os.environ.get("REST_COUNTRIES_API_KEY")
    if not API_KEY:
        print("No API key found. Set REST_COUNTRIES_API_KEY and try again.")
        exit()

    url= 'https://api.restcountries.com/countries/v5?response_fields=names.common,capitals,region,population'
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        countries = response.json()["data"]["objects"]
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        exit()
    return countries

def clean_countries(countries):
    cleaned_countries=[]
    for country in countries:
        cleaned_countries.append({
            "name":country["names"]["common"], 
            "capital":country["capitals"][0]["name"] if country.get("capitals") else "N/A", 
            "region":country["region"], 
            "population":country["population"]
            })
    return cleaned_countries

def menu():
    while True:
        choice = input(f"=== Country Explorer==="
              "\n 1. Search by name"
              "\n 2. Filter by region"
              "\n 3. Quit"
              "\n Choose an option (1-3): ")
        try:
            valid_choice = int(choice) in [1,2,3]
            if valid_choice == False:
                raise ValueError
            return int(choice)
        except TypeError, ValueError:
            print(f"\n Not a valid option. Try again. \n")

def search_by_name(cleaned_countries):
    country_name= input(f"\nEnter a country name: ")
    matches = [country for country in cleaned_countries if country_name.lower() in country["name"].lower()]
    if matches:
        print(f"\n")
        for match in matches:
            print(f"{match["name"]} - "
                f"Capital: {match["capital"]} | "
                f"Region: {match["region"]} | "
                f"Population: {match["population"]:,}")
        print(f"\n")
    else:
        print(f"\n {country_name} not found.\n")

def filter_by_region(cleaned_countries):
    available_regions = sorted({country["region"] for country in cleaned_countries})
    while True:
        region=input(f"\nRegion options include {available_regions}."
                 f"\nEnter a region: ").capitalize()
        if region in available_regions:
            matching_countries = [{"name":country["name"], "population":country["population"]}
                                for country in cleaned_countries if country["region"]==region]
            sorted_countries = sorted(matching_countries, key=lambda country: country["population"], reverse=True)
            print(f"\n")
            for country in sorted_countries:
                print(f"{country["name"]}: Population = {country["population"]:,}")
            print(f"\n")
            return
        else:
            print(f"\nNot a valid region. Try again.\n")

cleaned_countries = clean_countries(get_countries())
while True:
    choice = menu()
    if choice == 1:
        search_by_name(cleaned_countries)
    elif choice ==2:
        filter_by_region(cleaned_countries)
    else:
        print(f"\nThank you! Goodbye.\n")
        exit()



