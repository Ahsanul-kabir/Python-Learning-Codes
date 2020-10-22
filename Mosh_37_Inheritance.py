
# Inheritance holo existing code ke bar bar use kora
class Phone:       # Super Class, Parent Class, Base Class
    def call(self):
        print('You Can call')

    def message(self):
        print('You Can message')


class Samsung(Phone):      # Sub Class, Child Class, Derived Class
    # Call and Message Method come in Samsung
    def photo(self):
        print('You can take photo')






print('For Phone ::::')
P = Phone()
P.message()
P.call()
print('\n')


print(issubclass(Samsung,Phone))



print('\n' + 'For Samsung ::::')
S = Samsung()
S.call()
S.message()
S.photo()



