import requests
url = requests.get("https://api.mfapi.in/mf")

# print(url.json())

mydata = url.json()

# for i in mydata:
#     print(i)

print(mydata[0]["schemeCode"])