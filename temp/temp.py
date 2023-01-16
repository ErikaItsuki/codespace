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

def convert():

    while True:
        try:
            middle_endian = input("Date: ").strip().title()
            mm,dd,yyyy = re.split('[ -/.]', middle_endian)
            dd, yyyy = int(dd), int(yyyy)

            for month in months: # month = key, # months[month] = value
                if mm == month: # 'January' == 'January' , for exmaple -> passes to line 28
                    mm = months[month]

            return f"{yyyy}-{mm}-{dd}"

        except ValueError: # september(mm) -> 9(dd) included
            continue

print

################ HOW TO DO PSETS EFFICIENTLY #################
# read question
# get familiar with stuff from "hints"
# think with small, organized pieces and test each step of pieces (40 min)
# discord for more information
# final answer probably comes out here
