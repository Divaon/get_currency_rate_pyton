from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/load_currency_rate_on_date', methods=['GET'])
def currency_rate_on_date():
    date = request.json.get('date')
    result = date
    return jsonify("Successful load currency rate on date="+date)

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000
    )
