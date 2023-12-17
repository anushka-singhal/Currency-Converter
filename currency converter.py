with open ('currency.text') as f:
    lines = f.readlines()
    
currencyDict = {}
for line in lines:
    parsed = line.split("\t")
    currencyDict[parsed[0]] = parsed[1]
    
print(currencyDict)
amount = int(input("Enter the amount:"))
print("Enter the country you want to convert this amount from the given list:")
[print(item) for item in currencyDict.keys()]
currency = input("Enter the name of currency you want to convert")
print(f"{amount} INR is equal to {amount*float(currencyDict[currency])} {currency}")