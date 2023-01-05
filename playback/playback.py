string = input().strip().replace(" ", "...")
print(string)

################# delete before submission!!! ###################
""" another approach, poor though XD
# get input and print original

strings = input().strip().split(sep = " ")
print(strings)


# modify original string with a newly created list

playbacks = []
for string in strings[:len(strings)-1]:
    playbacks.append(string + "...")
playbacks.append(strings[len(strings)-1])


# print items of whole list

for playback in playbacks:
    print(playback, end = "")
"""
