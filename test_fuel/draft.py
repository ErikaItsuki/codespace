def main():

     while fraction := input("Fuel: ").strip():
          if convert(fraction) != True:
               pass # as long as while sees "break", not "no code to execute here", it continues
          else:
               percentage =
     #print(gauge(percentage))

def convert(fraction):

          try:
               x, y = fraction.split("/")
               percentage = int(x)/int(y) * 100
               if 0 < percentage < 100:
                    return round(percentage) # 4/3 return None != False: reprompt
          except(ValueError, ZeroDivisionError, NameError):
               return False

if __name__ == "__main__":
     main()