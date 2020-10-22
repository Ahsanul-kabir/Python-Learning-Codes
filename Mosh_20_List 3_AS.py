"""
Qus: Convert String to List then add Entered all numbers...

"""

n = input("Enter a text of numbers : ")  # 10 20 30 40
List = n.split()   # 10, 20, 30 ,40
sum =  0

for num in List:
    sum = sum + int(num)
print(sum)
