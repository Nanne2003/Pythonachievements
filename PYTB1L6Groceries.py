grocerylist = ("melk", "kaas", "worst", "boter", "water")
shoppingcart = ("melk", "kaas", "broccoli", "kipfilet")

a = set(grocerylist)
b = set(shoppingcart)

if a == b:
    print("Done shopping")
else:
    print("Continu shopping")