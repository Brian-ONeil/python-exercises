#!/usr/bin/env python
# coding: utf-8

# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[4]:


test_input = '2'


# In[5]:


if test_input == 2 or test_input == '2':
    print(True)


# In[6]:


def is_two(string):
    if string == 2 or string == '2':
        return True
    else:
        return False


# In[ ]:


Define a function named is_vowel. It should return True if the passed 
string is a vowel, False otherwise.


# In[41]:


is_vowel = ['a', 'e', 'i', 'o', 'u']


# In[83]:


is_vowel = input('Enter a vowel ')
if is_vowel in ['a', 'e', 'i', 'o', 'u']:
    print ('True')
else:
    print('False')


# In[7]:


def is_vowel(string):
    string_vowels = 'aeiou'
    
    if type(string) == str:
        return string.lower() in list(string_vowels)
    else:
        return False


# In[8]:


is_vowel('a')


# In[ ]:


Define a function named is_consonant. It should return True if the 
passed string is a consonant, False otherwise. Use your is_vowel 
function to accomplish this.


# In[84]:


is_consonant = input('Enter a consonant ')
if is_consonant in ['a', 'e', 'i', 'o', 'u']:
    print ('False')
else:
    print('True')


# In[9]:


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


# In[10]:


is_consonant('b')


# In[ ]:


Define a function that accepts a string that is a word. The function 
should capitalize the first letter of the word if the word starts with
a consonant.

word = 'hello'
# In[52]:


consonants = 'bcdfghjklmnpqrstvwxyz'


# In[85]:


def capitalize_consonant(word):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    if word and word[0].lower() in consonants:
        return str.capitalize()
    else:
        return word


# In[12]:


def capital_cons_start(string):
    if is_consonant(string[0]): #calling my is_consonant function
        string = string.capitalize()
    return string


# In[13]:


capital_cons_start('coffee')


# In[ ]:


Define a function named calculate_tip. It should accept a tip 
percentage (a number between 0 and 1) and the bill total, and return 
the amount to tip.


# In[15]:


tip_perc = .2
bill_total = 10


# In[16]:


bill_total * tip_perc + bill_total


# In[18]:


def calculate_tip(bill_total, tip_perc=.2):
    return bill_total * tip_perc + bill_total


# In[19]:


calculate_tip(100.00)


# In[ ]:


Define a function named apply_discount. It should accept a original 
price, and a discount percentage, and return the price after the 
discount is applied.


# In[20]:


og_price = 10
discount = .9


# In[21]:


og_price - og_price * discount


# In[23]:


def apply_discount(og_price, discount):
    return og_price - og_price * discount


# In[24]:


apply_discount(10,.6)


# In[ ]:


Define a function named handle_commas. It should accept a string that 
is a number that contains commas in it as input, and return a number 
as output.


# In[25]:


string_number = '1,000,000'


# In[27]:


def handle_commas(string_number):
    return int(string_number.replace(',',''))


# In[28]:


handle_commas("1,234")


# In[ ]:


Define a function named get_letter_grade. It should accept a number 
and return the letter grade associated with that number (A-F).


# In[29]:


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


# In[30]:


get_letter_grade(100)


# In[ ]:


Define a function named remove_vowels that accepts a string and 
returns a string with all the vowels removed.


# In[31]:


def remove_vowels(string):
    new_string = ''

    for char in string:
        if not is_vowel(char):
            new_string += char
            
    return new_string


# In[32]:


remove_vowels('hello')


# #### Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# 
# anything that is not a valid python identifier should be removed
# leading and trailing whitespace should be removed
# everything should be lowercase
# spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# In[33]:


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


# In[34]:


normalize_name('Name')


# In[ ]:


# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.

cumulative_sum([1, 1, 1]) returns [1, 2, 3]
cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]


# In[ ]:


ls = [1,1,1]


# In[35]:


def cumulative_sum(ls):
    total = 0 
    some_sums = []

    for numb in ls:
    #     print(numb)
        total += numb
#         print(total)
        some_sums.append(total)

    return some_sums


# In[36]:


cumulative_sum([1, 1, 1])


# In[ ]:




