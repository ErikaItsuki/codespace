def main():

    # align

    # thousand operate
    e = f'{12345:,}'
    print(e) # 12,345 (type == str)

    # expressing a %
    f = 1/10 # 0.1
    f = "{:.3%}".format(f) # 3 means how many d.p
    print(f) # 10.000%

    # type-specific formatting


main()