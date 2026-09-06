print("\n \n")
a = input("Hey user! What do you want to know(news/weather): ").lower()


if(a=="weather"):
    import requests
    
    API_KEY = "38afd32706f602c2c826252b70143b99"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    
    city = input("Enter city name: ")
    
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    
    response = requests.get(url)
    data = response.json()
    
    if data.get("cod") == 200:
        main = data["main"]
        weather = data["weather"][0]
        temperature = main["temp"]
        humidity = main["humidity"]
        description = weather["description"]
    
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print(f"Error: {data.get('message', 'Unknown error')}")


elif(a=="news"):
    import requests
    API_KEY = "3cb6db9305632e69f166f7a7fbd5173b"
    BASE_URL = "https://gnews.io/api/v4/top-headlines"
    params = {
    "country": "in",   # India headlines
    "lang": "en",      # English
    "token": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

# ✅ Concise terminal output
    if "articles" in data:
        print("\n📰 Top Headlines:\n")
        for article in data["articles"][:10]:  # limit to 10 headlines
            print(f"- {article['title']}")
    else:
        print("Error:", data.get("errors", "Unknown issue"))




else:
    print("Error occured in input!")
