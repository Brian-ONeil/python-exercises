is_two = 2
is_two = input('What is_two')
if is_two == str(2):
    print ('True')
else:
    print('False')

is_vowel = ['a', 'e', 'i', 'o', 'u'] 

is_vowel = input('Enter a vowel ')
if is_vowel in ['a', 'e', 'i', 'o', 'u']:
    print ('True')
else:
    print('False')

is_consonant = input('Enter a consonant ')
if is_consonant in ['a', 'e', 'i', 'o', 'u']:
    print ('False')
else:
    print('True')

def capitalize_consonant(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    if word and word[0].lower() in consonants:
        return str.capitalize()
    else:
        return word
    
tip_amount = .2

calculate_tip = input('Enter Bill')
def calculate_tip(tip_percentage, bill_total):
        tip_amount = bill_total * tip_percentage
        print(tip_amount)

original_price = 10
discount_percentage = .9

def apply_discount(original_price, discount_percentage):
    discount = original_price * (discount_percentage / 100)
    discounted_price = original_price - discount
    return discounted_price

function_handle_commas(str):
    str_without_commas = str.replace(",", "")
    num = convert_string_to_number(str_without_commas)
    return num

test_input = '2'

if test_input == 2 or test_input == '2':
    print(True)
    
def is_two(string):
    if string == 2 or string == '2':
        return True
    else:
        return False
    