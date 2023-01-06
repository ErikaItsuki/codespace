# ignore not denomination: insert : 7 -> insert:

# if insert = 25 or insert = 10 or insert = 5: insert -> Amount due = f() -> insert
# if amount_due - insert <= 0: break
amount_due = 50

# pay until >= 50
while (amount_due > 0): # continue

    amount_due -= int(input("Insert Coin: "))
    print(f"Amount Due: {amount_due}")




