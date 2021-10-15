from requests import get, utils


response = utils.get_unicode_from_response(get("http://www.cbr.ru/scripts/XML_daily.asp"))


def currency_rates(code):
    content = response.split("<Valute ID=")
    for i in content:
        if code.upper() in i:
            print(code.upper(), end=" ")
            return float(i.replace("/","").split("<Value>")[-2].replace(",", "."))# ("/","") слэш заменяем на пустую строку, split разбивает строко по value. replace меняет , на .

print(currency_rates("usd"))
print(currency_rates("eur"))


