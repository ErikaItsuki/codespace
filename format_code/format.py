def main():

    """access arguments means using args from like sth.format('a', 'b', 'c')"""

    # access by position
    a = '{2}, {1}, {0}'.format('a', 'b', 'c')
    print(a) # c, b, a

    # access by name
    b = 'coordinate:({x}, {y})'.format(x = '3', y = '5') # more clear in longer code
    """WRONG: b = 'coordinate:({x}, {y})'.format(___'3', ___'5'): must have x, y as names"""
    print(b) # coordinate:(3, 5)

    # access args'attr # after u KO classes :)


    # access args' items (whenever you see the word 'item', it correlates a list)
    coord = (3, 5)
    coord1 = [4, 6]
    d = 'coord = ({0[0]}, {0[1]}) and coord1 = ({1[0]}, {1[1]})'.format(coord, coord1)
    print(d) # coord = (3, 5) and coord = (4, 6)

    # align

    # thousand operate

    # expressing a %

    # type-specific formatting


main()