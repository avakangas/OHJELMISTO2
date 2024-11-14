import requests

def hae_saa(paikkakunta, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        saatilat = data['weather'][0]['description']
        temperatura = data['main']['temp']
        return saatilat, temperatura
    else:
        print("Virhe:", response.json())
        return None, None

if __name__ == "__main__":
    api_key = "avan_api_key"
    paikkakunta = input("Anna paikkakunnan nimi: ")

    saatilat, temperatura = hae_saa(paikkakunta, api_key)

    if saatilat is not None:
        print(f"Säätilanne: {saatilat.capitalize()}")
        print(f"Lämpötila: {temperatura} °C")
    else:
        print("Säätiedot eivät ole saatavilla. Tarkista paikkakunnan nimi.")
