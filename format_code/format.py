import datetime

def main():

    # type-specific formatting # Not know how to do with the types yet 
    d = datetime.datetime(2010, 7, 4, 12, 15, 58)
    d = '{:%-%m-%d %H:%M:%S}'.format(d)
    print(d) # %m-04 12:15:58 # missing %- for %Y which as a placeholder

main()