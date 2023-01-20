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

inside_colons = []
start = msg.find(":") # str.find() ; # list.index()

for char in msg[start:]: # a bit hard to use a for
                            # but if so, msg[start:len(msg)] only gives you a str
    if char != ":":
        inside_colons = inside_colons.append(char)
    else:
        inside_colons = inside_colons.append(":")
        break
print(inside_colons)

# too many var
# try not to use break

"""finally: print(f"output: {hello, fcall()}")"""
