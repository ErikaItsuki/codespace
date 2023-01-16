groceries = []

while True:
    try:
        item = input().strip().upper()
        groceries = sorted(groceries.append(item))
    except EOFError:
        break
    #else: # but if nothing goes wrong , go ahead and do this (else)

