amount_due = 50

while(amount_due > 0):
    print("Amount Due: 50")
    insert = int(input("Insert Coin: "))

    if insert == 25 or insert == 10 or insert == 5:
        amount_due -= insert

