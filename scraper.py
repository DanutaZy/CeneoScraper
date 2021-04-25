import requests
respons= requests.get('https://www.ceneo.pl/52404834#tab=reviews')
print (respons.status_code)