name = input("What's your name")

file = open("names.txt", "a", )
file.write(f"{name}\n") # if input("What's your name: ") inside {} -> 3 probs:
                        # "(" was not closed
                        # Unterminated expression in f-string; missing close brace
                        # "(" was not closed
                        # ????????? WHY ??????????
file.close()