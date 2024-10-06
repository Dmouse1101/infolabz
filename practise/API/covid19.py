#go to terminal download package : pip install requests.
import requests
# keys :
# tested
# statewise
# cases_times_series

url = requests.get("https://data.covid19india.org/data.json")
mydata = url.json()
# print(mydata)

for i in mydata:
    print(i)

print(mydata["cases_time_series"][0]["date"])

print(mydata["cases_time_series"][1]["dailyconfirmed"])