import requests
url = 'https://api.exchangerate-api.com/v6/latest'

req = requests.get(url)
print(req.status_code)

datas = req.json()
print(datas)

value_BRL = float(input("Informe o valor em R$ a ser convertido:\n"))
currency_quote = datas ['rates']['BRL']
print (f'R$ {value_BRL} em dólar valem US$ {(value_BRL / currency_quote):.2f}')