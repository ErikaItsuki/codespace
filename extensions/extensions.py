string = (input("File name: ")).strip().lower().split('.')

if string[1] == "gif":
    print("image/gif")
elif string[1] == "jpg" or "jpeg":
    print("image/jpeg")
else:
    print("application/octet-stream")