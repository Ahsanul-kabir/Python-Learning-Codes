
# Dictionary te Key Should be unique

customer = {
    "name" : "John Smith" ,
    "age" : 30 ,
    "is_verified" : True
}
print(customer["name"])
print('\n')


customer["name"] = "Aj Style"
print(customer["name"])
print('\n')


print(customer.get("birthdate")) # Another Way to access value
print(customer.get("birthdate" , "Jan 1 1980"))  # Dumy ekta text Pass kora holo eta kaj jdi kono vlue na pai


print('\n')
print(customer)
print('\n')

customer["birthdate"] = "Jan 1 1970"
print(customer["birthdate"])