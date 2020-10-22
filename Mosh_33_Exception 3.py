
def voter(age):
    if age < 18:
        raise ValueError("Invalid Error age is less then 18..")
    return "You are allowed to Vote"

voter(17)


"""
# we can also Handal like as below
def voter(age):
    if age < 18:
        raise ValueError("Invalid Error age is less then 18..")
    return "You are allowed to Vote"

try:
    print(voter(17)
except ValueError as e:
    print(e)

"""