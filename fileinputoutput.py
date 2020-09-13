filename = "fileforfileio.txt"
accessmode = 'w+'
UserInput = input("What you want to enter : \n")

file = open(filename, mode = accessmode)
file.write(UserInput)
#2 times write write is allowed. So need to close he file
file.write("\n")
UserInput = input("What else you want to enter : \n")
file.write(UserInput)
file.close()
file = open(filename, 'r+')

# filecontent = file.read()
# print(filecontent)

filecontentline = file.readline()
print(filecontentline)
file.close()