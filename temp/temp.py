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

        break
    except ValueError: # september(mm) -> 9(dd) included
        continue

if mm in months.keys():
    for month in months:
        if month == mm:
            mm == months[month]

print(f"{yyyy}-{mm}-{dd}")



# month accept str/int
# day and year accept int

""" ok but have another approach
if mm in months:
     for i in range(len(months)):
         if months[i] == mm:
             mm = i # no prob
"""