import requests

def main():
    """1"""
    print(f"{123456789.12345:,}") # WHAT IF 123,456.12345 : with decimal?

    # PROB1 cannot be used tgt (one at the front or end or even separated cuz 2)
    # PROB2 once a number is formatted by 1 formate code, it becomes a str so the
        # second formate code cuz error

    """2"""
    #print(f'{:,}'.format(123456)) # PROB: expected expression (:)
    value = '{:,}'.format(1234567890) # BUT not out of printf :)
    print()



main()
"""for key in o:
    print(key, end = "") # prints the whole dict # but not a prob"""