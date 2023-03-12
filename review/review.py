def main():

    bitcoin = {
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

    # METHOD_1
    for item in bitcoin["bpi"]["USD"]:
        if item == "rate":
            print(bitcoin["bpi"]["USD"][item])

    #METHOD_2
    #for item in bitcoin["bpi"]:
        # inner = list(bitcoin["bpi"]) # list(key) -> 'USD'


main()