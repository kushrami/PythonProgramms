Count = 0 
for Count in range(10):
    Count = Count + 1
    for InsideCount in range(10):
        InsideCount = InsideCount + 1
        print(Count,"*",InsideCount,"=",InsideCount*Count)
for Count in range(10,20):
    Count = Count + 1
    for InsideCount in range(10):
        InsideCount = InsideCount + 1
        print(Count,"*",InsideCount,"=",InsideCount*Count)
for Count in range(20,30,2):
    Count = Count + 1
    for InsideCount in range(10):
        InsideCount = InsideCount + 1
        print(Count,"*",InsideCount,"=",InsideCount*Count)
for Count in [22,24,26,28,30]:
    
    for InsideCount in range(10):
        InsideCount += 1
        print(Count,"*",InsideCount,"=",InsideCount*Count)

for Count in ['red','green','blue']:
    for InsideCount in ['red','green','blue']:
        print(Count,InsideCount)

answer = '0'
while answer != '4':
    answer = input("What is 2+2 : ")

print("Good!")