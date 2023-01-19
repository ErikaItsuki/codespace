import re

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        outdated = input("date: ").strip().title()
        if '/' in outdated:
            mm,dd,yyyy = int(outdated.split("/"))

        elif ' ' in outdated: # corner = Sep 8 ,1636
                                      # to handle the corner at the same time: replace , to nothing then split, not afterwards
            mm,dd,yyyy = outdated.replace(",", "").split()# what if replace has found no ,?
        else:
            continue

        dd,yyyy = int(dd), int(yyyy)

        if 1 <= dd <= 31 and  yyyy >= 0:

            if mm in months: # mm = str
                mm = months.index(mm) + 1
            elif 1 <= int(mm) <= 12: # mm is int # int(mm) directly returns sth,
                                     # no need to be stored so a new var not needed
                mm = int(mm)
        else:
            continue

    except ValueError:
        continue

    else:
        print(f"{yyyy}-{mm:02}-{dd:02}") # if mm is str, print 0 AFTER mm
        break



"""
if all int:
    unchange
elif mm == str, and other == int:
    mm to int
else:
    reprompt

"""
# if outdated.isalpha

""" not good
mm, dd, yyyy = input().strip().tilte().split('/') # deal with format /
if mm.isalpha():
    continue
else:
    int(mm,dd,yyyy)

except ValueError:
    mm,dd,yyyy = outdated.replace(",", "").split()
    if mm in months: # format must be ' ' ', ' # but mm is not defined cuz unpacking failed
        mm = months.index(mm) + 1 ## 8 8, 1936
        int(mm,dd,yyyy)

    else:
        continue
else:
    if 1 <= dd <= 31 and  yyyy >= 0 and 1 <= mm <= 31:
        return f"{yyyy}-{mm:02}-{dd:02}"
    else:
        ##continue##

"""