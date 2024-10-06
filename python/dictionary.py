# python : DICTIONARY

# 1) currly braces required.
# 2) Group of :- key : value.
# 3) access using key to print value in it.
# 4) use key when data is in {} and number(index) when [].

# 1
mydata ={"Gujarat": "Gandhinagar", "Rajasthan": "jaipur"}
print(mydata["Rajasthan"])

# 2
mydata2 = {"ahmedabad": 100, "surat": [200, 233, 0], "rajkot": 300}
print(mydata2["surat"][1])  # information gain in surat

# 3
mydata3 = {"ahmedabad": [{"date": "19 june 23", "cases": 25},  # multiple data in curly braces
                        {"date": "20 june 23", "cases": 35},
                        {"date": "21 june 23", "cases": 45}],
                        "surat": [200, 255, 0],  # multiple data in square braces
                        "rajkot": 310
                        }
print(mydata3["ahmedabad"][1]["date"])
print("Cases are : "+mydata3["ahmedabad"][2]["date"])