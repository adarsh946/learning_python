
with open("donkey.txt", "r") as f :
    content = f.read()
    modified_content = content.replace("donkey", "#####")

with open("donkey.txt", "w") as f :
    f.write(modified_content)