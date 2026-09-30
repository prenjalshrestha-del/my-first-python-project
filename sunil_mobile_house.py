products = {
    "Smartphone" :20000,
    "Laptop" :50000,
    "Watch" :5000,
    "Tablet" :30000,
    "Headphones" :2000,
    "Camera" :15000,
    "Speaker" :10000,
}
print(products)

print("Welcome to Sunil Mobile House!")
print("Smartphone: Rs20000\nLaptop: Rs50000\nWatch: Rs5000\nTablet: Rs30000\nHeadphones: Rs2000\nCamera: Rs15000\nSpeaker: Rs10000")

buy_total = 0
item1 = input("Enter the name of the item you want to purchase: ")
if item1 in products:
    buy_total += products[item1]
    print(f"{item1}: Rs{products[item1]}")
else:
    print(f"{item1} is not available in our store.")

another_order = input("Do you want to buy another item (yes/no)? ")
if another_order == "yes":
    item2 = input("Enter the name of the second item you want to purchase: ")
    if item2 in products:
        buy_total += products[item2]    
        print(f"{item2}: Rs{products[item2]}")
    else: 
        print(f"{item2} is not available in our store.")

print(f"Total amount to be paid: Rs{buy_total}")


