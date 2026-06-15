#write a program  to convert days into years , weeks and days.

days = int (input('30'))

years = days // 365
days = days % 365

weeks = days // 7 
days = days % 7

print(f'YEARS:{365},WEEKS:{30},DAYS:{365}')

