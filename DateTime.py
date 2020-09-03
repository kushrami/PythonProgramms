import datetime
CurrentDate = str(datetime.date.today())

# print(CurrentDate.year)
# print(CurrentDate.month)
# print(CurrentDate.day)

# birthday = input("Please Enter your next birthday in DD/MM/YYYY : ")
# birthday = datetime.datetime.strptime(birthday, '%m/%d/%Y').date()
# print(birthday)

# DayAreLeft = birthday - datetime.datetime.strptime(CurrentDate,'%m/%d/%Y').date()
# print(DayAreLeft.days)
#play around and correct it. 

CurrentTime = datetime.datetime.now()
print(CurrentTime)