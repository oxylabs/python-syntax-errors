prices = {"price1": 9.99, "price2": 13.48 "price3": 10.99, "price4": 15.01}
price_found = False
for key value in prices.items():
    if 10 <= value <= 14.99:
        print(key + ":", value)
        price_found = True
if not price_found:
    print("There are no prices between $10 and $14.99")