def main():
    strings = (input("File name: ")).strip().lower().split('.')
    print(media_type(strings))

# image
def media_type(strings):

    last_index = len(strings) - 1

    if strings[last_index] == "gif" or strings[last_index] == "png":
        return f"image/{strings[last_index]}"

    elif strings[last_index] == "jpg" or strings[last_index] == "jpeg":
        return "image/jpeg"


    # application

    elif strings[last_index] == "pdf" or strings[last_index] == "zip":
        return f"application/{strings[last_index]}"


    # text

    elif strings[last_index] == "txt":
        if strings[0] == "plain":
            return "text/plain"
        else:
            return f"text/{strings[last_index]}"

    else:
        return "application/octet-stream"

main()