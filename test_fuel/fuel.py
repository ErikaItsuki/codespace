def main():

    fraction = input("Fraction: ").strip()
    gauge(convert(fraction))

def convert(fraction):

     while True:
          try:
               x, y = fraction.split("/")
               fraction = int(x)/int(y) * 100
               if 0 < fraction < 100:
                    return f"{:.%}".format(fraction)

          except(ValueError, ZeroDivisionError, NameError):
               pass

def gauge(percentage):
     if  percentage <= 1:
          print("E")
     elif percentage >= 99:
          print("F")
     else:
          print(f"{round(fraction)}%")
