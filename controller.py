
import zlib
from flask import Flask, request, jsonify
from repository_currency import get_currency_by_date_from_nbrb, get_currency_by_date_and_code_from_nbrb

app = Flask(__name__)




# endpoint which load exchange rate to db on date by url .../load_exchange rate_on_date?date={our_date}
@app.route('/load_exchange rate_on_date', methods=['GET'])
def exchange_rate_on_date():
    date = request.args.get('date')
    result = get_currency_by_date_from_nbrb(date)
    if result == "Error":
        return jsonify("Error on load exchange rate on date=" + date)
    return jsonify("Successful load exchange rate on date="+date)

# endpoint which load exchange rate to db and return to browser on date by currency code and use url .../load_exchange_rate_by_code_on_date?date={our_date}&currency_code={currency code}
@app.route('/load_exchange_rate_by_code_on_date', methods=['GET'])
def exchange_rate_by_code_on_date():
    date = request.args.get('date')
    currency_code = request.args.get('currency_code')
    result = get_currency_by_date_and_code_from_nbrb(date, currency_code)
    if result == "Error":
        return jsonify("Error on load exchange rate on date=" + date+" code=" + currency_code + " ")
    response_body = "Successful load exchange rate on date=" + date + " code=" + currency_code + " " + str(result)
    crc = zlib.crc32(response_body.encode()) & 0xffffffff
    return jsonify(response_body), 200, {'CRC32': str(crc)}



if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000
    )
