https://replit.com/join/roueywmxsm-lucasleite32

wands = ["1. Elder Wand", "2. Hawthorn Wand", "3. Willow Wand", "4. Holly Wand", "5. NONE"]
t_customer = 0
c_buys = 0
Elder_Wand = 0
Hawthorn_Wand = 0
Willow_Wand = 0
Holly_Wand = 0

customer = input("Does the customer come in? yes/no ").lower()
print()

while customer == "yes":
    t_customer += 1

    print("What wand does the customer want to buy?")
    print()
    for wand in wands:
        print(wand)
    buy = int(input())

    if 1 <= buy <= 4:
        print("The customer bought a wand")
        print()
        c_buys += 1

        if buy == 1:
            Elder_Wand += 1
          
        elif buy == 2:
            Hawthorn_Wand += 1
          
        elif buy == 3:
            Willow_Wand += 1
          
        elif buy == 4:
            Holly_Wand += 1
          
    else:
        print("The customer did not buy a wand")
        print()
    customer = input("Does the customer come in? yes/no ").lower()
    print()

not_buys = t_customer - c_buys

print(t_customer, "customer(s) came to the store")
print(c_buys, "customer(s) who bought a wand")
print(not_buys, "customer(s) who did not buy a wand")
print()
print(f"Today, {Elder_Wand} Elder Wand, {Hawthorn_Wand} Hawthorn Wand, {Willow_Wand} Willow Wand, {Holly_Wand} Holly Wand were sold")
