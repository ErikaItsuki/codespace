amount_due = 50
print(f"Amount Due = {amount_due}")

while(amount_due > 0):
    insert = int(input("Insert Coin: "))
    if insert == 25 or insert == 10 or insert == 5:
        amount_due -= insert
        print(f"Amount Due = {amount_due}")


print(f"Change Owed = {-amount_due}")




