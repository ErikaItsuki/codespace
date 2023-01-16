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

middle_endian = input("Date: ").strip()
mm,dd,yyyy = re.split('[ -/.]', middle_endian)


# month accept str/int
# day and year accept int

if mm in months:
    for i in range(len(months)):
        if months[i] == mm:
            mm = i # no prob
            
print(f"{yyyy} {mm} {dd}")