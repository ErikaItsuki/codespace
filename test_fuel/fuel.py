def main():

    fraction = input("Fraction: ").strip()
    convert(fraction)

def convert(fraction):

     while True:
          try:
               x, y = fraction.split("/")
               fraction = int(x)/int(y) * 100
               if 0 < fraction < 100:
                    return fraction:.%

          except(ValueError, ZeroDivisionError, NameError):
               pass

def gauge(percentage):
     if fraction <= 1:
          print("E")
     elif fraction >= 99:
          print("F")
     else:
          print(f"{round(fraction)}%")
