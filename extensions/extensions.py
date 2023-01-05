strings = (input("File name: ")).strip().lower().split('.')
last_index = len(strings) - 1

# image
def 
if strings[last_index] == "gif" or strings[last_index] == "png":
    return f"image/{strings[last_index]}"

elif strings[last_index] == "jpg" or strings[last_index] == "jpeg":
    print("image/jpeg")


# application

elif strings[last_index] == "pdf" or strings[last_index] == "zip":
    print(f"application/{strings[last_index]}")


# text

elif strings[last_index] == "txt":
    if string[0] == "plain":
        print("text/plain")
    else:
        print(f"text/{strings[last_index]}")

else:
    print("application/octet-stream")

