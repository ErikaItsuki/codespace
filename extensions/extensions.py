string = (input("File name: ")).strip().lower().split('.')

if string[1] == "gif":
    print("image/gif")
elif string[1] == "jpg" or "jpeg":
    print("image/jpeg")
else:
    # if one word: append sth for it # or if len(string) != 2: print sth
    print("application/octet-stream")