
'''
    AND : both Condition should be true
    OR : at least one should be true
    NOT: Inverse any value

    Question:
    if application has high income And good credit Eligible for loan
'''

has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")



print('\n')
has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

