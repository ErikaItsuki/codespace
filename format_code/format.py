import datetime

def main():

    # type-specific formatting
    d = datetime.datetime(2010, 7, 4, 12, 15, 58)
    """is equivalent to"""
    d = '{:%-%m-%d %H:%M:%S}'.format(d)
    print(d)

main()