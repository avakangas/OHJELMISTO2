import requests

def hae_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        vitsi_data = response.json()
        return vitsi_data['value']
    else:
        return "Vitsin hakeminen epäonnistui."

if __name__ == "__main__":
    vitsi = hae_vitsi()
    print(vitsi)
