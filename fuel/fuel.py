# prompt in a loop

while True:

     try:
        # if x <= y : x and y are compared in str
        # x, y = int(x), int(y) # exception handled here
        # what if they input negatives?
        x, y = input("Fraction: ").split("/")
        fraction = int(x)/int(y) * 100
        if fraction < 0 or fraction > 100:
            continue

     except(ValueError, ZeroDivisionError, NameError):
        pass # if pass -> repeatedly informing the user the Error (of print) from except

     else:
        if fraction <= 1:
             print("E")
        elif fraction >= 99:
             print("F")
        else:
             print(f"{round(fraction)}%")
        break
 #       else: # handling negative here -> weird!!! --> so i put into try ~~
 #           continue

