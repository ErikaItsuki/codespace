import emoji
"""
input = input("Input: ").strip()

if "_" in input:
    print(f"Output: {emoji.emojize(input)}")
else:
    print(f"Output: {emoji.emojize(input)}", language = "alias")
"""
# like whatsapp:
# read the whole msg
# if :sth: found -> replace the whole :sth: with emoji.emojize(:sth:)

### to find out the substring with ::###
msg = list(input("Input: ").strip())

sub = []
start = msg.index(":") # str.find() ; # list.index()
for i in msg[start:len(msg)]:
    sub = sub.append(msg[i])
    if msg[i] == ":":
        sub = sub.append(msg[i])
        break
print(sub)



