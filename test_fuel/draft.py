def main():
    ...

def convert(fraction):
    while fuel := input("Fuel: ").strip():
        try:
            x, y = fuel.split("/")
            fraction = int(x)/ int(y) *100
        except (ValueError, ZeroDivisionError):
            pass

if __name__ == "__main__":
     main()