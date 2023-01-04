def main():
    height = int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n): # i starts from 0: n = 3 means [0, 1, 2]
        print(i, end = " ")
        print("#"*i) # a smarter approach

if __name__ == "__main__":
    main()

