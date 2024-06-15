import requests

from currency_dao import add_currency_rate_to_database


# get data abot currency by date from https://api.nbrb.by
def get_currency_by_date_from_nbrb(date):
    responce=requests.get("https://api.nbrb.by/exrates/rates?ondate="+date+"&periodicity=0")
    if responce.status_code==404:
        return "Error"
    for line in responce.json():
        add_currency_rate_to_database(line)
    return

# get data abot currency by date and currency code from https://api.nbrb.by
def get_currency_by_date_and_code_from_nbrb(date, currency_code):
    responce=requests.get("https://api.nbrb.by/exrates/rates/"+currency_code+"?ondate="+date)
    line = responce.json()
    if responce.status_code==404:
        return "Error"
    add_currency_rate_to_database(line)
    return line