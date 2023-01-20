import emoji

""" Draft
input = input("Input: ").strip()

if "_" in input:
    print(f"Output: {emoji.emojize(input)}")
else:
    print(f"Output: {emoji.emojize(input)}", language = "alias")
"""

""" Purpose of the EX: like whatsapp:
read the whole msg
if :sth: found -> replace the whole :sth: with emoji.emojize(:sth:)"""


""""""""""""""""""""""""""""""""""""""""""


### to find out the substring with ::###

msg = list(input("Input: ").strip())

inside_colons = [":"]
start = msg.index(":") # str.find() ; # list.index()


for char in msg[start + 1:]: # a bit hard to use a for
                            # but if so, msg[start:len(msg)] only gives you a str
    if char != ":":
        inside_colons.append(char) # the whole thing if assigned to a var => becomes NoneType:
                                   # inside_colons = None
                                   # in the next loop: None.append(char of i+1) will be invalid
                                   # REASON: python append does not return any value to the user.
    else:
        inside_colons.append(":") # keep append alone all the time ;)
        break

msg = str(msg).replace(inside_colons, emoji.emojize(str(inside_colons)))
print(msg)


# too many var
# try not to use break

"""finally: print(f"output: {hello, fcall()}")"""
