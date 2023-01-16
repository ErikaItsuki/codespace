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
        middle_endian = input("Date: ").strip()
        mm,dd,yyyy = re.split('[ -/.]', middle_endian)
        dd, yyyy = int(dd), int(yyyy)

        break
    except ValueError: # september(mm) -> 9(dd) included
        continue

if mm in months:
     for i in range(len(months)):
         if months[i] == mm:
             mm = i # no prob

print(f"{yyyy}-{mm}-{dd}")



# month accept str/int
# day and year accept int

