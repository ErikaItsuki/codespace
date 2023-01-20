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

msg = input("Input: ").strip()

inside_colons = ":"
start = msg.find(":") # str.find() ; # list.index()


for char in msg[start + 1:]: # a bit hard to use a for
                            # but if so, msg[start:len(msg)] only gives you a str
    if char != ":":
        inside_colons = inside_colons + char # the whole thing if assigned to a var => becomes NoneType:
                                   # inside_colons = None
                                   # in the next loop: None.append(char of i+1) will be invalid
                                   # REASON: python append does not return any value to the user.
    else:
        inside_colons = inside_colons + ":" # keep append alone all the time ;)
        break


msg, inside_colons = str(msg), str(inside_colons)
# str(msg) = str([":", ..."]) = "[":", ....]" # simply adding a pair of quotes
# if you are directly printing out the list elmnts like in camel,
# that is much easier, but here we've got to change it back
# and here is where unfamiliar
msg = msg.replace(inside_colons, emoji.emojize(inside_colons))# emojize keeps str unchanged
                                                                             # if the str matches nothing
print(str(msg))


# too many var
# try not to use break
# why not string till the end?

"""finally: print(f"output: {hello, fcall()}")"""
