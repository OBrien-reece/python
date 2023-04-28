# OR
# AND
# NOT

# has_high_income = False
# has_good_credit = True
#
#  if has_good_credit and has_high_income:
#      print('Eligible for a loan')
#  print('Not eligible for a loan')
#
# if has_good_credit or has_high_income:
#     print('Eligible for a loan')
# else:
#     print('Not eligible for a loan')

has_good_credit = True
has_criminal_record = True

if has_good_credit and not has_criminal_record:
    print('Eligible for a loan')
else:
    print('Not Eligible for a loan')