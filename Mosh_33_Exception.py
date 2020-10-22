
"""
 # ZeroDivisionError :
num = input("Enter a number : ")
result = 20 / num
print(result)
print("Done")



 # Type Error :
num = input("Enter a number : ")
result = 20 / num
print(result)
print("Done")


# IndexOutOfBound(Index Error)
text = "Anis"
print(text[4]
print("Done")


"""


try:
    list = [20,0,30]
    result = list[0] / list[1]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by is not possible")
except IndexError:
        print("Indext error")

finally:
    print("Successful")
