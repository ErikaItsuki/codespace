import sys
import csv
from tabulate import tabulate

try:
    if len(sys.argv) == 2:
        if sys.argv[1].endswith(".csv"):
             with open(sys.argv[1]) as file:
                """reader = csv.reader(file)
                print(tabulate(reader, headers = "firstrow", tablefmt = "grid"))"""
                dictreader = csv.DictReader(file)
                print(tabulate(dictreader, headers = "keys", tablefmt = "grid"))

        else:
            sys.exit("Not a CSV file")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else:
        sys.exit("Too few command-line arguments")

except FileNotFoundError:
    sys.exit("File does not exist")
