from requests import get

print("NBP currency calculator")

data_all_currency = get("https://api.nbp.pl/api/exchangerates/tables/a/?format=json")
data_all_currency_json = data_all_currency.json()

amount_of_currencies = len(data_all_currency_json[0]["rates"])  # ilosc walut
# print(data_single_currency_json["rates"][0]["mid"]) #  test

a = True
while a:
    user_currency_code = input("Jaką walute chcesz sprawdzić? ").upper()

    # czy kod waluty istnieje
    for x in range(0, amount_of_currencies):
        if user_currency_code == data_all_currency_json[0]["rates"][x]["code"]: #  warunek sprawdzajacy czy istnieje
            a = False
            break
        elif amount_of_currencies == x and a is True:  # jeśli nie jest
            print("Nie ma takiego kodu waluty")

data_single_currency = get(f"https://api.nbp.pl/api/exchangerates/rates/a/{user_currency_code}/2021-06-01/?format=json")
data_single_currency_json = data_single_currency.json()
print(data_single_currency_json)
