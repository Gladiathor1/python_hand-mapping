import os

for filename in os.listdir("./images"):
    # if filename.endswith(".asm") or filename.endswith(".py"):
    #      # print(os.path.join(directory, filename))
    #     continue
    # else:
    #     continue
    data = filename.split(".")
    print(data[0])
    textfile = open(data[0]+".txt", "w+")