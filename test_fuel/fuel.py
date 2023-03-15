def main():

    fraction = input("Fraction: ").strip()
    gauge(convert(fraction))

def convert(fraction):

     while True:
          try:
               x, y = fraction.split("/")
               fraction = int(x)/int(y) * 100
               if 0 < fraction < 100:
                    return "{:.%}".format(fraction)
          except(ValueError, ZeroDivisionError, NameError):
               continue

def gauge(percentage):
     if  percentage <= 1:
          print("E")
     elif percentage >= 99:
          print("F")
     else:
          print(f"{round(percentage)}%")

if __name__ == "__main__":
     main()