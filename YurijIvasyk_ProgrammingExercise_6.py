#code takes phone numbers, social security, and zip codes and validates them using regular expressions
import re

#function that tests phone number format
def phone_check(p):
    pattern = r'\d\d\d-\d\d\d-\d\d\d\d'

    #output based off correct/wrong format
    if re.match(pattern, p):
        print('Format good, good job, very good, very nice.')
    else:
        print('Wrong format.')

#function that tests social security format
def social_check(s):
    pattern = r'\d\d\d-\d\d-\d\d\d\d'

    #output based off correct/wrong format
    if re.match(pattern, s):
        print('Format good, good job, very good, very nice.')
    else:
        print('Wrong format.')

#function that tests zip code format
def zip_check(z):
    pattern = r'\d\d\d\d\d'

    #output based off correct/wrong format
    if re.match(pattern, z):
        print('Format good, good job, very good, very nice.')
    else:
        print('Wrong format.')

#main function takes user input and runs it through regular expression functions to check for correct format
def main():
    #UI initialization
    print('Hi, please enter your phone number, social security, and zip code')

    phone = input('phone number: ')
    phone_check(phone)

    social = input('social security: ')
    social_check(social)

    zipcode = input('zip code: ')
    zip_check(zipcode)

main()