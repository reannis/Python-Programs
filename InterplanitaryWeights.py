#planet gravity coefficiens

nMERCURY = .38
nVENUS = .91
nMOON = .165
nMARS = .38
nJUPITER = 2.34
nSATURN = .93
nURANUS = .92
nNEPTUNE = 1.12
nPLUTO = .066

sname = input("what is your name? ")
fweight = float(input("what do you weigh on earth? (in lbs) "))

#for testing

#print(fweight)


print(f'your weight on Mercury is {fweight * nMERCURY:15.2f}')
print(f'your weight on Venus is {fweight * nVENUS:15.2f}')
print(f'your weight on the moon is {fweight * nMOON:15.2f}')
print(f'your weight on Mars is {fweight * nMARS:15.2f}')
print(f'your weight on Jupiter is {fweight * nJUPITER:15.2f}')
print(f'your weight on Saturn is {fweight * nSATURN:15.2f}')
print(f'your weight on Uranus is {fweight * nURANUS:15.2f}')
print(f'your weight on Neptune is {fweight * nNEPTUNE:15.2f}')
print(f'your weight on Pluto is {fweight * nPLUTO:15.2f}')
