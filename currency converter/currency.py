import requests

API_KEY='fca_live_5BJ1GlAVT7aqHgbduVKdB5pKySnatdlhLgNURsZK'
BASE_URL=f'https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}'

CURRENCIES = ['USD', 'CAD', 'EUR', 'AUD', 'CNY']

def convert_currency(base):
  currencies = ','.join(CURRENCIES)
  # 上面的公式則會變成 'USD, CAD, EUR, AUD, CNY'
  url = f'{BASE_URL}&base_currency={base}&currencies={currencies}'
  try:
    response = requests.get(url)
    data = response.json()
    # print(data)
    return data['data']
  except:
    print('Invalid currency!')
    return None

while True:  
  base = input('Enter the base currency (q for quit): ').upper()

  if base  == 'Q':
    break

  data = convert_currency(base)
  if not data:
    continue

  del data[base]
  # print(data)
  for ticker, value in data.items():
    print(f'{ticker}: {value}')