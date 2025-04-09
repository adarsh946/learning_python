
# st = "wow you are again going in the direction of hell or is this the way of Heaven. actually I'm little confused. yeah! whhat should I do??"

# f = open("text1.txt","w")
# f.write(st)



# f.close()

# f = open("text1.txt")
# text = f.readline()
# print(text, type(text))
# f.close()

f = open("text1.txt", "r")
text = f.readline()
while(text != ""):
    print(text)
    text = f.readline()

f.close()