mm,dd,yyyy = input("date: ").split('/')
# split + unpack -> because input without 2 / returns numbers of chunks not equals 3
# if no / found, return the whole str is the only elmnt in the list
# and so cannot be copied