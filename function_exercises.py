def is_two(string):
    if string == 2 or string == '2':
        return True
    else:
        return False







def is_vowel(string):
    string_vowels = 'aeiou'
    
    if type(string) == str:
        return string.lower() in list(string_vowels)
    else:
        return False





def is_consonant(string):
    if type(string) == str:    
        if string.isalpha() == True:
            if not is_vowel(string):
                return True
            else:
                return False # this is false when the input is not a consonant
        else:
            return False # this is false when the input is not a letter
    else:
        return False #this is false when the input is not a string





def capitalize_consonant(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    if word and word[0].lower() in consonants:
        return str.capitalize()
    else:
        return word





def capital_cons_start(string):
    if is_consonant(string[0]): #calling my is_consonant function
        string = string.capitalize()
    return string




def calculate_tip(bill_total, tip_perc=.2):
    return bill_total * tip_perc + bill_total



og_price = 10
discount = .9



def apply_discount(og_price, discount):
    return og_price - og_price * discount




string_number = '1,000,000'


def handle_commas(string_number):
    return int(string_number.replace(',',''))





def get_letter_grade(grade):
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    else:
        letter_grade = 'F' 
        
    return letter_grade





def remove_vowels(string):
    new_string = ''

    for char in string:
        if not is_vowel(char):
            new_string += char
            
    return new_string





def normalize_name(string):
    string = string.strip().lower().replace(' ','_')
    
    new_string = ''

    for char in string:
    #     print(char)
        if char.isalpha() or char.isdigit() or char == '_':
    #         print('this is valid')
            new_string += char

    new_string = new_string.strip('_')
    
    return new_string


ls = [1,1,1]


def cumulative_sum(ls):
    total = 0 
    some_sums = []

    for numb in ls:
    #     print(numb)
        total += numb
#         print(total)
        some_sums.append(total)

    return some_sums







