groceries = []

while True:
    try:
        item = input().rstrip().upper()
        groceries.append(item)
    except EOFError:
        for item in sorted(groceries):
            print(item)
        break

