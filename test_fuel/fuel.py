def main():

     while fraction := input("Fraction: ").strip()
          try:
               x, y = fraction.split("/")
               fraction = int(x)/int(y) * 100
               if 0 < fraction < 100:
                    percentage = "{:.%}".format(fraction)
          except(ValueError, ZeroDivisionError, NameError):
               continue

    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):




def gauge(percentage):
     if  percentage <= 1:
         result = "E"
     elif percentage >= 99:
          result = "F"
     else:
          result = f"{round(percentage)}%"
     return result

if __name__ == "__main__":
     main()