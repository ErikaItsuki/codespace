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

while True:
    try:
        middle_endian = input("Date: ").strip()
        mm,dd,yyyy = re.split('[ -/.]', middle_endian)

    except valueError:
        continue
    else:
         if mm in months:
            print(f"{year}-{months[months.keys()]}-{day}")
            # months[months.keys()] should be valid