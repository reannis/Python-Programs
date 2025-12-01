import random
import string

while True:
    cha = abs(int(input('how many characters? ')))

    while cha > 40:
        print('')
        print('too many characters')
        print('')
        cha = abs(int(input('how many characters? ')))

        
    else:
        
        special_characters = '#!@$%^&+=-_\/?<>'

        alpha_numeric = list(string.ascii_lowercase + string.ascii_uppercase + string.digits + special_characters)

        password = ''

        def generate(password):
            for i in range(cha):
                c = random.choice(alpha_numeric)
                password = password + c
            print(password)
                
        generate(password)
     

    new_request = input('Ready for a new password request? (yes/no): ').lower()
    
    if new_request != 'yes':
        break
    
        print('')