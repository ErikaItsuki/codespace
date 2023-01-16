groceries = []

while True:
    try:
        item = input().rstrip().upper()
        groceries = sorted(groceries.append(item))
    except EOFError:
        groceries = sorted(groceries)
        break
    #else: # but if nothing goes wrong , go ahead and do this (else)

#printing the list after sorting
for i in range(len(groceries)):
    if groceries[i] == groceries[i-1]:
        counter += 1
    else:
        print(f"{i} {groceries[i-1]}")
        counter = 1

