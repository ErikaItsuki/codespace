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
counter = 1

def counting(i = 1): # call with counter()

    while(i < len(groceries)):
        if groceries[i] == groceries[i-1]:
            counter += 1
            i+=1
        else:
            counters.append(counter)
            counter = 1
            i += 1



"""ideas"""
# list.count(target) -> how we know the targets' names?