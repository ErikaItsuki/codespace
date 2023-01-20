import emoji

input = input("Input: ").strip()
input = ":"+ input +":"

print(f"Output: {emoji.emojize(input)}")
