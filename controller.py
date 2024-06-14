from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/load_exchange rate_on_date', methods=['GET'])
def exchange_rate_on_date():
    date = request.json.get('date')
    result = date
    return jsonify("Successful load exchange rate on date="+date)


@app.route('/load_exchange_rate_by_code_on_date', methods=['POST'])
def exchange_rate_by_code_on_date():
    date = request.json.get('date')
    currency_code = request.json.get('currency_code')
    result = date
    return jsonify("Successful load exchange rate on date="+date + " code="+currency_code)

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000
    )
