quantity = ""
if quantity == "":
    print("missing quantity")
else:
    try:
        quantity = int(quantity)
        print("valid quantity:",quantity)
    except ValueError:
        print("Invalid quantity:", quantity)