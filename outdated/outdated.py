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
         if mm in months:
            print(f"{year}-{months[months.keys()]}-{day}") # months[months.keys()] should be valid

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

""" from temp
import re

months = {
    "January" : "1",
    "February" : "2",
    "March" : "3",
    "April" : "4",
    "May" : "5",
    "June" : "6",
    "July" : "7",
    "August" : "8",
    "September" : "9",
    "October" : "10",
    "November" : "11",
    "December" : "12"
}
while True:
    try:
        middle_endian = input("Date: ").strip()
        mm,dd,yyyy = re.split('[ -/.]', middle_endian)
        dd, yyyy = int(dd), int(yyyy)
        if mm in months.keys():
            for month in months:
                if month == mm:
                    mm == months[month]
        break

    except ValueError: # september(mm) -> 9(dd) included
        continue


print(f"{yyyy}-{mm}-{dd}")



# month accept str/int
# day and year accept int

"""
"""
ok but have another approach
if mm in months:
     for i in range(len(months)):
         if months[i] == mm:
             mm = i # no prob
"""

# test cases:
# September 8 2022 -> ok
# 8 September 2022 -> ValueError
# 8 September 2022 -> No ValueError but
# may 2022 8 -> yyyymmdd XX 8-5-2022
"""