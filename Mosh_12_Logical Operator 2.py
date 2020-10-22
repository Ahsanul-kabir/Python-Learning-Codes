
'''
    if application has high income OR good credit Eligible for loan
'''

has_high_income = True
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")



print('\n')
has_high_income = False
has_good_credit = True

if has_high_income or has_good_credit:
    print("Eligible for loan")

