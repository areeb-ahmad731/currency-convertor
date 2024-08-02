
try:
    with open("currencydata.txt", "r") as f:
        lines = f.readlines()
except FileNotFoundError:
    print("File not found")
    exit(1)

currency_dict = {}
for line in lines:
    parsed = line.strip().split("\t")
    if len(parsed) < 2:
        print(f"Skipping line: {line}")
        continue
    currency_dict[parsed[0]] = parsed[1]
amount=int(input("enter the amount \n "))
#print(currency_dict)
print("enter the currency you want to convert to the given available options\n: ")
[print(item) for item in currency_dict.keys()]
currency=input("please enter one of the values;\n ")
print(f"{amount}INR is equal to  {amount*float(currency_dict[currency])} {currency}  "  )