import requests

from currency_dao import add_currency_rate_to_database


def get_currency_by_date_from_nbrb(date):
    responce=requests.get("https://api.nbrb.by/exrates/rates?ondate="+date+"&periodicity=0")
    for line in responce.json():
        add_currency_rate_to_database(line)
    return

def get_currency_by_date_from_nbrb(date, currency_code):
    responce=requests.get("https://api.nbrb.by/exrates/rates/"+currency_code+"?ondate="+date)
    line = responce.json()
    print(line)
    add_currency_rate_to_database(line)
    return line