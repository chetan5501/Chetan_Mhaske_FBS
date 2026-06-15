###

#input
l = int (input('Enter length:'))
b = int (input('Enter breadth:'))
r = int (input('Enter radius:'))

#operation

rec_per = 2*(l+b)
rec_area = l+b

hc_per = (1/2)*(2*3.14*r)
hc_area = (1*2)*(3.14*r*r)

perimeter = rec_per + rec_per
area = hc_area + hc_area

print('perimeter of figure:',perimeter)
print ('area of figure:',area )