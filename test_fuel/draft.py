def main():

     while fraction := input("Fuel: ").strip():
        try:
            percentage = convert(fraction)
        except ValueError:
            return ValueError

def convert(fraction):

          try:
               x, y = fraction.split("/")
               percentage = int(x)/int(y) * 100
               if 0 < percentage < 100:
                    return round(percentage) # 4/3 return None != False: reprompt
          except(ValueError, ZeroDivisionError):
               return ValueError

if __name__ == "__main__":
     main()