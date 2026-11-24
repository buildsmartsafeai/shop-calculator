from datetime import datetime
shop = {"mandazi": 20, "tea": 30, "bread": 60}

def add_tax(price):
    return round(price * 1.16, 2)

def discount_price(price):
    return round(price * 0.9, 2)


total = 0
while True:
    try:
        count = int(input("How many items? "))
        if count <= 0:
            print("Please enter a number above 0.")
            continue
        break
    except ValueError:
        print("Please enter a number, like 3.")
for i in range(count):
    choice = input("What do you want? ").lower().strip()

    if choice in shop:
        print(choice, "costs", shop[choice])
        total = total + shop[choice]
    else:
        print("Sorry, we don't sell that")

if total > 100:
    total = discount_price(total)

print("Total:", total)
print("With tax:", add_tax(total))
if total > 100:
    total = discount_price(total)

stamp = datetime.now().strftime("%d %B %Y, %H:%M")

print("Date:", stamp)
print("Total:", total)
print("With tax:", add_tax(total))

with open("receipts.txt", "a") as f:
    f.write("Date: " + stamp + "\n")
    f.write("Total: " + str(total) + "\n")
    f.write("With tax: " + str(add_tax(total)) + "\n")
    f.write("-----\n")
