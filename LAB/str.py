name = 'TeetatSunawat'
print(name[0:6])
print(name[6:13])

word = 'banana'
if word == 'banana':
    print("Alright, bananas.")

if word < 'banana':
    print('Your word,' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word,' + word + ', comes after banana.')
else:
    print('Alright, banana.')


data = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)
sppos = data.find(' ',atpos)
print(sppos)
host = data[atpos+1 : sppos]
print(host)