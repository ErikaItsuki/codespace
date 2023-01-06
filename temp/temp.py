amount_due = 50

while(amount_due > 0):# the condition was left empty at first
                       # knew after the modification in line 9
                       # PRETTY GOOD APPROACH :)
    print(f"Amount Due: {amount_due}")
    insert = int(input("Insert Coin: "))

    if insert == 25 or insert == 10 or insert == 5:
        amount_due -= insert

print(f"Change Owed: {-amount_due}")

