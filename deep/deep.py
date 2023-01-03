
x = str.lower(input("What is the answer...? ").strip()) # won't affect 42 ;)

if x == "42" or "forty-two" or "forty two":
    print("Yes")
else:
    print("No")

# all 3 test passed

# exception handling: all with whitespace, different cases converted into 2 conditions