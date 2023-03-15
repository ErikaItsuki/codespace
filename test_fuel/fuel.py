def main():

     while fraction := input("Fuel: ").strip()
          convert(fraction)

     convert(fraction)
     print(gauge(percentage))

def convert(fraction):

          try:
               x, y = fraction.split("/")
               fraction = int(x)/int(y) * 100
               if 0 < fraction < 100:
                    return "{:.%}".format(fraction)
          except(ValueError, ZeroDivisionError, NameError):
               continue

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