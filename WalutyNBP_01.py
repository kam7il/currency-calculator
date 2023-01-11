import sys
from datetime import datetime
from requests import get, JSONDecodeError

print("NBP currency calculator")

data_all_currency = get("https://api.nbp.pl/api/exchangerates/tables/a/?format=json")
data_all_currency_json = data_all_currency.json()

amount_of_currencies = len(data_all_currency_json[0]["rates"])  # ilosc walut
# print(data_single_currency_json["rates"][0]["mid"]) #  test

a = True
while a:
    user_currency_code = input("Jaką walute chcesz sprawdzić? ").upper()
    # user_currency_code = "EUR"

    # czy kod waluty istnieje
    for x in range(0, amount_of_currencies):
        if user_currency_code == data_all_currency_json[0]["rates"][x]["code"]: #  warunek sprawdzajacy czy istnieje
            a = False
            break
        elif amount_of_currencies == x and a is True:  # jeśli nie jest
            print("Nie ma takiego kodu waluty")


user_date_input = input("Podaj date (RRRR-MM-DD): ")
# user_date_input = "2020-01-02"

try:
    datetime.fromisoformat(user_date_input)
except ValueError:
    print("Błędny format daty lub data nie poprawna")
    sys.exit()

data_single_currency = get(f"https://api.nbp.pl/api/exchangerates/rates/a/{user_currency_code}/{user_date_input}/?format=json")

try:
    data_single_currency_json = data_single_currency.json()
    # print(data_single_currency_json)
except JSONDecodeError:
    print("Nie ma danych w podanej dacie")
    sys.exit()

print(data_single_currency_json[f"rates"][0]["mid"], "PLN za 1", user_currency_code)
