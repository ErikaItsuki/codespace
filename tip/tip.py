def main():
    dollars = dollars_to_float(input("How much was the meal? ").strip())
    percent = percent_to_float(input("What percentage would you like to tip? ").strip())
    print(f"Leave ${dollars * percent:.2f}")


def dollars_to_float(d):
    return float(d.lstrip('$'))

def percent_to_float(p):
    return float(p.rstrip('%')) * 0.01

main()