def main():
    
    fraction = input("Fraction: ").strip()
    convert(fraction)

def convert(fraction):

     while True:
          try:
               x, y = fraction.split("/")
               fraction = int(x)/int(y) * 100
               if 0 < fraction < 100:
                    return fraction

          except(ValueError, ZeroDivisionError, NameError):
               pass

def gauge(percentage):
     ...
