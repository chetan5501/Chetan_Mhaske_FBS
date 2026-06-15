gender = input ('Enter gender (M/F):')

age = int (input('Enter age:'))

if(gender == 'f'):
    if(age >= 18):
        print('Girl is eligibal for marriage.')
    else:
        print('pehle bade ho jao.')
else:
    if(age >= 21):
        print('Boy is eligibal for marriage.')
    else:
        print('Pehle kama lo.')