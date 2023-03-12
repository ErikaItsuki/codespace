def main():

    students = {
        "Gryff":{
            "Harry":{"number" : 1,"year" : 1},
            "Ron":{"number" : 2,"year" : 1}
        }
    }

    for house in students:
        print(house) # Griff
        # go to key = "Harry"
        for key in house["Harry"]:
            print(key)
        # print(students(stu)) # Harry, Ron # TypeError: dict obj not callable

"""    bitcoin = {
        "bpi": {
            "USD": {
            "code": "USD",
            "symbol": "&#36;",
            "rate": "20,893.7844",
            "description": "United States Dollar",
            "rate_float": 20893.7844
            }
        }
    }

    for item in bitcoin["bpi"]["USD"]:
        """

main()