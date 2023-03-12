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

    for item in bitcoin["bpi"]["USD"]:
        print(item["rate"])


main()