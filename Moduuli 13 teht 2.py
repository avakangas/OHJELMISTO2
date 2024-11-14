from flask import Flask, jsonify

app = Flask(__name__)

lentokentat = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EGLL": {"Name": "London Heathrow Airport", "Municipality": "London"},
    "EDDB": {"Name": "Berlin Brandenburg Airport", "Municipality": "Berlin"},
    "JFK": {"Name": "John F. Kennedy International Airport", "Municipality": "New York"},
    "LAX": {"Name": "Los Angeles International Airport", "Municipality": "Los Angeles"},
}

@app.route('/kenttä/<icao>', methods=['GET'])
def kentta(icao):

    if icao in lentokentat:
        kentta_tiedot = lentokentat[icao]
        kentta_tiedot["ICAO"] = icao
        return jsonify(kentta_tiedot)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
