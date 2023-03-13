import datetime

def main():

    """access arguments means using args from like sth.format('a', 'b', 'c')"""

    # access by position

    # access by name

    # access args'attr

    # access args' items

    #align

    #these two seems not capable to be in the same .py: first date is not def when import datatime but from...
    #print(date.fromisoformat('20230313')) #from YYYYMMDD or YYYY-MM-DD (or some cryptic hex-like syntax therein) to2023-03-13
    date = datetime.date(2019, 12, 4)
    print(date) # 2019-12-04
    print(date.__str__())



main()