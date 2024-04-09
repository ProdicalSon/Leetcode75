months = 'JanFebMarAprMayJunJulAugSepOctNovDec'
name = 'John Brian'
monthnum = input('Enter the number of the month to display (1 - 12)')
monthnum = int(monthnum)

startindex = (monthnum - 1)*3
endindex = startindex + 3

monthabbrv = months[startindex:endindex]
print(monthabbrv)
print('My name is '+ name+' and '+'I was born in the month of '+monthabbrv)

print()