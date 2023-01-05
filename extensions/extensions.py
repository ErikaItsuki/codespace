string = (input("File name: ")).strip().lower().split('.')
last_index = len(string) - 1

if string[last_index] == "gif" or string[last_index] == "jpg" or string[last_index] == "jpg"
    print("image/gif")
elif string[last_index] == "jpg" or "jpeg":
    print("image/jpeg")
elif string[last_index] == "png":
    print
elif string[last_index] == "pdf":
elif string[last_index] == "txt":
elif string[last_index] == "zip":

else:
    # if one word: append sth for it # or if len(string) != 2: print sth
    print("application/octet-stream")