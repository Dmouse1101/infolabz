import requests

url = requests.get("https://isro.vercel.app/api/spacecrafts")

# keys
# spacecrafts
# print(url.json())

for i in url.json():
    print(i)

print(url.json()["spacecrafts"][0]["name"])