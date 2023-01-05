strings = (input("File name: ")).strip().lower().split('.')
last_index = len(strings) - 1

if strings[last_index] == "gif" or strings[last_index] == "jpeg" or strings[last_index] == "png":
    print(f"image/{strings[last_index]}")
elif strings[last_index] == "jpg":
    print("image/jpeg")
elif strings[last_index] == "pdf" or strings[last_index] == "zip":
    print(f"application/{strings[last_index]}")
elif strings[last_index] == "txt":
    print(f"text/{strings[last_index]}")

else:
    # if one word: append sth for it # or if len(string) != 2: print sth
    print("application/octet-stream")

# normally multiple dots are invalid , but the prog allows multiple dots as delimiters
# What to do???