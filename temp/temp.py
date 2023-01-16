months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

mm = input().strip().title()
if mm in months: # input 4 ->  sys.exit here
                 # if mm in dict -> consider keys of the dict only
    if mm in months.keys():
        print(f"{mm} as a key")
    else:
        print(f"{mm} as a value")