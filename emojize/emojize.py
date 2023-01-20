import emoji

input = input("Input: ").strip()

if "_" in input:
    print(f"Output: {emoji.emojize(input)}")
else:
    print(f"Output: {emoji.emojize(input)}", language = "alias")

# like whatsapp:
# read the whole msg
# if :sth: found -> replace the whole :sth: with emoji.emojize(:sth:)

to_emoji = []

msg = list(input("Input: ").strip())
for i in range(len(msg)):
    if msg[i] == ":":
        to_emoji = to_emoji
