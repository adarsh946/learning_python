
with open("poem.txt") as f :
    content = f.read()
    if("Twinkle" in content):
        print(True)
    else: 
        print(False)

