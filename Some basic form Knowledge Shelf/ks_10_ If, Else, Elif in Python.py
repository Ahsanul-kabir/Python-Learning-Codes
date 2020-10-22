name = input("Please enter your name : ")
age = int(input("Aap ki age kay hai, {0}? ".format(name)))

print(age)

if age >= 18:
    print("Aap vote de sakte hai!!!")

else:
    print("Aap vote dalne ke liye {0} saal ke baad aaeye.".format(18 - age))