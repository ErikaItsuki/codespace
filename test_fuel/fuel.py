def main():
    x, y = input("Fraction: ").split("/")
    convert(x, y)

def convert(x, y):

     while True:
          try:
               fraction = int(x)/int(y) * 100
               if 0 < fraction < 100:
                    return fraction

          except(ValueError, ZeroDivisionError, NameError):
               pass

def gauge(percentage):
     