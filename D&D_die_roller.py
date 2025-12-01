import random

cont = True

def roll():
    if condition == 'advantage':
        if result1 >= result2:
            print(result1)
        else:
            print(result2)
    elif condition == 'disadvantage':
        if result1 >= result2:
            print(result2)
        else:
            print(result1)
                
    elif condition == 'none':
        print(result1)
    else:
        print('invalid input, try again')

while cont == True:
    max_ = abs(int(input('what is the maximum number? ')))

    result1 = random.randint(1, max_)
    result2 = random.randint(1, max_)
    #print(result1)    #for debugging
    #print(result2)    #same as above

    condition = input('conditions (advantage/disadvantage/none): ').lower()
    roll()
    try_ = input("Would you like to roll again? (Y/N) ")

    cont = try_ == "Y"
