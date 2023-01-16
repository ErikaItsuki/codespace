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
        middle_endian = input("Date: ").strip().title()
        mm,dd,yyyy = re.split('[ -/.]', middle_endian)
        dd, yyyy = int(dd), int(yyyy)

    except ValueError: # september(mm) -> 9(dd) included
        continue
    else:
        for month in months: # month = key, # months[month] = value
            if mm == months:
                mm == months[month]

        break

print(f"{yyyy}-{mm}-{dd}")

