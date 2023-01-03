#PyPI : python package index : download, store in folder...like IDLEs
#but py has its own package managing system : pip
# doesn't come with python itself
import cowsay
import sys

if len(sys.argv) == 2:  # only if the human gives you 1 name, it will cont.
    cowsay.("hello, " , sys.argv[1])






