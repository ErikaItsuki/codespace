import re

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


# check ValueError:
while True:
    try:
        middle_endian = input("Date: ").strip()
        mm,dd,yyyy = re.split('[ -/.]', middle_endian)




    except valueError:
        continue
    else:
         if mm in months.keys():
            print(f"{year}-{months[months.keys]}-{day}")

"""
MM : str/int
DD -> int ->
YYYY ->

September 8 1636
September 8, 1636
split by spaces, then eliminate any punctuation

9/8/1636
9-8-1636

slash/ hyphen- period.

"""
""" input --> split --> convert --> rearrange

return f"{year}-{month}-{day}"
"""

