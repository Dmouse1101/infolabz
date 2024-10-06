mydata = {"maharashtra":{"mumbai":{"city":"metro city","metro":"yes"},"popluation":"20 cr"},
          "gujarat":["Ahmedabad","Surat","Rajkot"],
          "rajasthan":['Ajmer',"jaisalmer",{"capital":"jaipur"},["Mewad","RJ","INR"]]
          }

print(mydata["maharashtra"]["mumbai"]["city"])
print(mydata["rajasthan"][2]["capital"])
print(mydata["gujarat"][2])
print(mydata["rajasthan"][3][1])