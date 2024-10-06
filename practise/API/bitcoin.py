import requests

url = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# print(url.json())
mydata = url.json()
for i in mydata:
    print(i)

print(mydata["bpi"]["USD"]["rate"])