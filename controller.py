import traceback
import zlib

import psycopg2
from flask import Flask, request, jsonify

from repository_currency import get_currency_by_date_from_nbrb

app = Flask(__name__)





@app.route('/load_exchange rate_on_date', methods=['GET'])
def exchange_rate_on_date():
    date = request.json.get('date')
    get_currency_by_date_from_nbrb(date)
    return jsonify("Successful load exchange rate on date="+date)


@app.route('/load_exchange_rate_by_code_on_date', methods=['POST'])
def exchange_rate_by_code_on_date():
    date = request.json.get('date')
    currency_code = request.json.get('currency_code')
    result = get_currency_by_date_from_nbrb(date, currency_code)
    response_body = "Successful load exchange rate on date=" + date + " code=" + currency_code + " " + str(result)
    crc = zlib.crc32(response_body.encode()) & 0xffffffff
    return jsonify(response_body), 200, {'CRC32': str(crc)}

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000
    )
