def main():

     while fraction := input("Fuel: ").strip()
          try:
               percentage = convert(fraction)
          except(ValueError, ZeroDivisionError, NameError):
               continue

     convert(fraction)
     print(gauge(percentage))

def convert(fraction):

     x, y = fraction.split("/")
     fraction = int(x)/int(y) * 100
     if 0 < fraction < 100:
          return "{:.%}".format(fraction)


def gauge(percentage):
     if  percentage <= 1:
         result = "E"
     elif percentage >= 99:
          result = "F"
     else:
          result = f"{round(percentage)}%"
     return restult

if __name__ == "__main__":
     main()