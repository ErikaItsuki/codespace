groceries = []

while True:
    try:
        item = input().strip().upper()
        groceries = sorted(groceries.append(item))
    except EOFError:
        break
    #else: # but if nothing goes wrong , go ahead and do this (else)

#printing the list after sorting

counters = []
i = 1 # if i != i-1 -> return counter = 1
counter = 1
while(i < len(groceries)):
    if groceries[i] == groceries[i-1]:
        counter += 1
    else:
        counters.append(counter)

for i in range(len(groceries)):

        counter += 1
    else:
        print(f"{i} {groceries[i-1]}")
        counter = 1

"""ideas"""
# list.count(target) -> how we know the targets' names?