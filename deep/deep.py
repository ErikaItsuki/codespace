x = str.lower(input("What is the answer...? ").strip()) # won't affect 42 ;)

if x == "42" or "forty-two" or "forty two":
    print("Yes")
else:
    print("No")

# all 3 test passed

# exception handling: all with whitespace on either side, different cases converted into 2 conditions
# case 1:    42 # whitespace in both L and R             # passes
# case 2: Forty two # whitespace in mid, and first cap   # passes
# case 3: Forty-TWO # cap no only the first              # passes


