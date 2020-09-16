import sys
firstnumber = float(input("First Number :"))

SecondNumber = float(input("Second Number :"))

try:
    result = firstnumber / SecondNumber
    print("result = ",result)
except ZeroDivisionError:
    try:
        file = open("errorlog.txt","w+")
    except:
        print("No file for logging.")
    error = sys.exc_info()[0]
    file.write(str(error))
    sys.exit()
    print("There is something wrong in your input")
#finally is always run. sys.exit() also can't skip it.
finally:
    print("Exit!")
#we can try and except this in opening file and your library and all. It will be great. 

