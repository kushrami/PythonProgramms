#this is an empty list
Host = ['kush',"shweta","dipak","gayathri"]

for Count in Host:
    print(Count)

UserCall = input("Please enter name that you want to call : ")

for Count in Host:
    if UserCall == Count:
        Host.remove(UserCall)
        print("He is removed!")
    else:
        print("No one is there.")

UserAddition = input("Please enter the name of person you want to add : ")

Host.append(UserAddition)

print("Please Check the list below: ")
lengthofhost = len(Host)
for Count in range(lengthofhost):
    print(Host[Count])

print(Host.index('kush'))
Host.sort()
print(Host)
