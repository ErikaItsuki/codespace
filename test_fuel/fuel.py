def main():

     fraction = input("Fuel: ").strip():
     percentage = convert(fraction)
     print(gauge(percentage))

def convert(fraction):

     try:
          x, y = fraction.split("/")
          percentage = int(x)/int(y) * 100
          if 0 < percentage < 100:
               return round(percentage) # 4/3 return None != False: reprompt
     except(ValueError, ZeroDivisionError):
          raise ValueError("expected int/int not zero")

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