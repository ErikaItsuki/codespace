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

sub = []
start = msg.index(":") # str.find() ; # list.index()
current = start
while (current < len(msg)): # a bit hard to use a for
                            # but if so, msg[start:len(msg)] only gives you a str
    if msg[current] != ":":
        sub = sub.append(msg[current])
    else:
        sub = str(sub.append(":"))
        break
print(sub)

# too many var
# try not to use break

"""finally: print(f"output: {hello, fcall()}")"""
