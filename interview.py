total = 0.0
counter = 0

# enter time in loop
while True:
    try:
        time = input("Time for 10km (press Enter for mean): ").strip()
        if not time:
            break # directly exit loop if enter is pressed
        time = int(time)

    except ValueError:
        continue
    else:
        total += time
        counter += 1



# exit loop and print average
print(f"average time of {counter} runs = {total/counter}")
